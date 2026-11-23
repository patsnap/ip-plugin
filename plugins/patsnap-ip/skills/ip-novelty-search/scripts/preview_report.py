#!/usr/bin/env python3
"""Preview one existing HTML report in a local browser; do not serve its workspace."""

import argparse
import json
import shutil
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


def make_server(report, port=0):
    report = Path(report).resolve(strict=True)
    if not report.is_file() or report.suffix.lower() not in {".html", ".htm"}:
        raise ValueError("Preview requires an existing HTML report")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.respond(head=False)

        def do_HEAD(self):
            self.respond(head=True)

        def respond(self, *, head):
            route = urlsplit(self.path).path
            if route not in {"/", "/report.html", "/download"}:
                self.send_error(404)
                return
            try:
                source = report.open("rb")
            except OSError:
                self.send_error(404, "Report is unavailable")
                return
            with source:
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(report.stat().st_size))
                self.send_header("Cache-Control", "no-store")
                self.send_header("X-Content-Type-Options", "nosniff")
                disposition = "attachment" if route == "/download" else "inline"
                self.send_header(
                    "Content-Disposition", f'{disposition}; filename="report.html"'
                )
                self.end_headers()
                if not head:
                    shutil.copyfileobj(source, self.wfile)

        def log_message(self, format, *args):
            pass

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True)
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    server = make_server(args.file, args.port)
    url = f"http://127.0.0.1:{server.server_port}"
    print(
        json.dumps(
            {"preview_url": url + "/report.html", "download_url": url + "/download"}
        ),
        flush=True,
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
