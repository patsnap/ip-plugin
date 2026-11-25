# Patsnap Searchable Fields

> 字段和语法用于构建检索式；实际调用以工具schema为准，未执行的语法需标明待验证。参见[工具使用要点](tool-usage.md)。

Source: `智慧芽可搜索字段.docx`, parsed into a reusable field reference for the skill.

Total fields identified: 269.

Use this file when the user asks for a Patsnap executable search formula or when mapping a retrieval idea to exact searchable fields. Prefer the source document if the user provides an updated version.

## Category Summary

| Category | Field count |
| --- | ---: |
| 号码&文本 | 47 |
| 公司&人 | 47 |
| 日期&分类 | 55 |
| 引用&同族 | 21 |
| 专利状态&质量 | 36 |
| 诉讼 | 30 |
| 许可 | 7 |
| 权利转移 | 4 |
| 复审无效 | 12 |
| 质押 | 7 |
| 工作空间 | 3 |

## 号码&文本

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `PN` | 公开(公告)号 | 号码 | PN:US1234567 |
| `APNO` | 申请号 | 号码 | APNO:US10/123456 |
| `PRNO` | 优先权号 | 号码 | PRNO:JP2013270967 |
| `KD` | 文献代码 | 号码 | KD:B1 |
| `PCT_PN` | PCT国际申请公开号 | 号码 | PCT_PN:WO2017161368 |
| `PCT_APNO` | PCT国际申请申请号 | 号码 | PCT_APNO:US2017/023191 |
| `FAM_ID` | 简单同族编号 | 号码 | FAM_ID:138860071 |
| `IFAM_ID` | INPADOC同族编号 | 号码 | IFAM_ID:438860071 |
| `EFAM_ID` | 智慧芽同族编号 | 号码 | EFAM_ID:742326667 |
| `TTL` | 标题 | 文本 | TTL:汽车 |
| `ABST` | 摘要 | 文本 | ABST:汽车 |
| `CLMS` | 权利要求 | 文本 | CLMS:汽车 |
| `ICLMS` | 独立权利要求 | 文本 | ICLMS:car 仅支持英文语言专利及受理局为CN的专利 |
| `DESC` | 说明书 | 文本 | DESC:汽车 |
| `DESC_F` | 技术领域 | 文本 | DESC_F:汽车 仅支持受理局为CN的专利搜索 |
| `DESC_B` | 背景技术 | 文本 | DESC_B:汽车 仅支持受理局为CN的专利搜索 |
| `DESC_S` | 发明内容 | 文本 | DESC_S:汽车 仅支持受理局为CN的专利搜索 |
| `DESC_D` | 附图说明 | 文本 | DESC_D:汽车 仅支持受理局为CN的专利搜索 |
| `DESC_E` | 具体实施方式 | 文本 | DESC_E:汽车 仅支持受理局为CN的专利搜索 |
| `PROBLEM_SUM` | 技术问题 | 文本 | PROBLEM_SUM:透气性差 支持搜索有说明书文本的全球专利 |
| `METHOD_SUM` | 技术手段 | 文本 | METHOD_SUM:汽车 支持搜索有说明书文本的全球专利 |
| `BENEFIT_SUM` | 技术功效 | 文本 | BENEFIT_SUM:汽车 支持搜索有说明书文本的全球专利 |
| `PROBLEM_PHR` | [标]技术问题短语 | 文本 | PROBLEM_PHR:成本高 仅支持受理局为CN/US/EP/WO专利搜索 |
| `BENEFIT_PHR` | [标]技术功效短语 | 文本 | BENEFIT_PHR:降低成本 仅支持受理局为CN/US/EP/WO专利搜索 |
| `TA` | 标题/摘要 | 文本 | TA:(汽车 and 座椅) |
| `TAC` | 标题/摘要/权利要求 | 文本 | TAC:(汽车 and 座椅) |
| `TACD` | 标题/摘要/权利要求/说明书 | 文本 | TACD:(汽车 and 座椅) |
| `MAINF` | 主要字段 | 文本 | MAINF:汽车 主要字段包括标题、摘要、权利要求、说明书、公开号、申请号、申请人、发明人和IPC/UPC/LOC分类号 在检索式中，如果没有指定字段，则默认在“主要字段”的范围中进行搜索 |
| `TTL_ENTRANS` | 英文机翻标题 | 文本 | TTL_ENTRANS:car |
| `ABST_ENTRANS` | 英文机翻摘要 | 文本 | ABST_ENTRANS:car |
| `CLMS_ENTRANS` | 英文机翻权利要求 | 文本 | CLMS_ENTRANS:car |
| `ICLMS_ENTRANS` | 英文机翻独立权利要求 | 文本 | ICLMS_ENTRANS:car |
| `DESC_ENTRANS` | 英文机翻说明书 | 文本 | DESC_ENTRANS:car |
| `TTL_CNTRANS` | 中文机翻标题 | 文本 | TTL_CNTRANS:汽车 |
| `ABST_CNTRANS` | 中文机翻摘要 | 文本 | ABST_CNTRANS:汽车 |
| `CLMS_CNTRANS` | 中文机翻权利要求 | 文本 | CLMS_CNTRANS:汽车 |
| `ICLMS_CNTRANS` | 中文机翻独立权利要求 | 文本 | ICLMS_CNTRANS:汽车 |
| `DESC_CNTRANS` | 中文机翻说明书 | 文本 | DESC_CNTRANS:汽车 |
| `TTL_ALL` | 标题原文和翻译 | 文本 | TTL_ALL:汽车 |
| `ABST_ALL` | 摘要原文和翻译 | 文本 | ABST_ALL:汽车 |
| `CLMS_ALL` | 权利要求原文和翻译 | 文本 | CLMS_ALL:汽车 |
| `ICLMS_ALL` | 独立权利要求原文和翻译 | 文本 | ICLMS_ALL:汽车 |
| `DESC_ALL` | 说明书原文和翻译 | 文本 | DESC_ALL:汽车 |
| `TA_ALL` | 标题/摘要原文和翻译 | 文本 | TA_ALL:汽车 |
| `TAC_ALL` | 标题/摘要/权利要求原文和翻译 | 文本 | TAC_ALL:汽车 |
| `TACD_ALL` | 标题/摘要/权利要求/说明书原文和翻译 | 文本 | TACD_ALL:汽车 |
| `MAINF_ALL` | 主要字段原文和翻译 | 文本 | MAINF_ALL:汽车 主要字段原文和翻译包括标题原文和翻译、摘要原文和翻译、权利要求原文和翻译、说明书原文和翻译、公开号、申请号、申请人、发明人和IPC/UPC/LOC分类号 |

## 公司&人

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `ALL_AN` | [全字段]申请(专利权)人 | 文本 | ALL_AN:清华大学 [全字段]申请(专利权)人: 联合索引字段, 检索结果包括以下五个字段: [标]当前申请(专利权)人、当前申请(专利权)人、[标]原始申请(专利权)人、原始申请(专利权)人、历史申请(专利权)人 |
| `AN` | 原始申请(专利权)人 | 文本 | AN:清华大学 原始申请(专利权)人：专利最初的申请(专利权)人 |
| `ANC` | 当前申请(专利权)人 | 文本 | ANC:清华大学 当前申请(专利权)人：专利当前的申请(专利权)人 |
| `ANS` | [标]原始申请(专利权)人 | 文本 | ANS:清华大学 [标]原始申请(专利权)人：经智慧芽标准化处理后的专利最初的申请(专利权)人 |
| `ANS_EXACT` | 精准[标]原始申请(专利权)人 | 文本 | ANS_EXACT:清华大学 精准匹配[标]原始申请(专利权)人；符号、大小写字母等全匹配 |
| `ANCS` | [标]当前申请(专利权)人 | 文本 | ANCS:清华大学 [标]当前申请(专利权)人：经智慧芽标准化处理后的专利当前申请(专利权)人 |
| `ANCS_EXACT` | 精准[标]当前申请(专利权)人 | 文本 | ANCS_EXACT:清华大学 精准匹配[标]当前申请(专利权)人；符号、大小写字母等全匹配 |
| `AN_HIST` | 历史申请(专利权)人 | 文本 | AN_HIST:清华大学 包括专利转移、变更过程中、专利质押、担保过程中存在过的申请(专利权)人 |
| `GNAME` | 自定义申请人组 | 文本 | GNAME:清华大学 |
| `AN_ADD` | 原始申请(专利权)人地址 | 文本 | AN_ADD:北京 |
| `AN_COUNTRY` | 原始申请(专利权)人区域 | 文本 | AN_COUNTRY:CN AN_COUNTRY:中国 使用申请人国家/地区名或者代码搜索 |
| `AN_PROVINCE` | 原始申请(专利权)人州/省 | 文本 | AN_PROVINCE:江苏 AN_PROVINCE:32 使用省份名或代码搜索 仅支持受理局为CN的专利搜索 |
| `AN_CITY` | 原始申请(专利权)人地市 | 文本 | AN_CITY:南京 使用中国地市或美国市镇搜索 仅支持受理局为CN、美国专利搜索 |
| `AN_DISTRICT` | 原始申请(专利权)人区县 | 文本 | AN_DISTRICT:鼓楼区 使用中国区县或美国郡县搜索 仅支持受理局为CN、美国专利搜索 |
| `ANC_ADD` | 当前申请(专利权)人地址 | 文本 | ANC_ADD:北京 |
| `ANC_COUNTRY` | 当前申请(专利权)人区域 | 文本 | ANC_COUNTRY:CN ANC_COUNTRY:中国 使用申请人国家/地区名或者代码搜索 |
| `ANC_PROVINCE` | 当前申请(专利权)人州/省 | 文本 | ANC_PROVINCE:江苏 ANC_PROVINCE:32 使用省份名或代码搜索 仅支持受理局为CN的专利搜索 |
| `ANC_CITY` | 当前申请(专利权)人地市 | 文本 | ANC_CITY:南京 使用中国地市或美国市镇搜索 仅支持受理局为CN、美国专利搜索 |
| `ANC_DISTRICT` | 当前申请(专利权)人区县 | 文本 | ANC_DISTRICT:鼓楼区 使用中国区县或美国郡县搜索 仅支持受理局为CN、美国专利搜索 |
| `F_AN` | 第一原始申请(专利权)人 | 文本 | F_AN:清华大学 |
| `F_ANC` | 第一当前申请(专利权)人 | 文本 | F_ANC:清华大学 |
| `ANS_TYPE` | [标]原始申请(专利权)人类型 | 文本 | ANS_TYPE:ACADEMY ACADEMY: 院校/研究所 COMPANY: 公司 GOVERNMENT: 政府机构 PERSON: 个人 HOSPITAL: 医院 BANK: 银行 |
| `ANCS_TYPE` | [标]当前申请(专利权)人类型 | 文本 | ANCS_TYPE:ACADEMY ACADEMY: 院校/研究所 COMPANY: 公司 GOVERNMENT: 政府机构 PERSON: 个人 HOSPITAL: 医院 BANK: 银行 |
| `IN` | 发明人 | 文本 | IN:李书福 |
| `INC` | 当前发明人 | 文本 | INC:李书福 进行过发明人变更后的当前发明人名称 仅支持受理局为CN的专利搜索 |
| `IN_EXACT` | 精准发明人 | 文本 | IN_EXACT:李书福 精准匹配发明人；符号、大小写字母等全匹配 |
| `IN_ADDRESS` | 发明人地址 | 文本 | IN_ADDRESS:北京 |
| `F_IN` | 第一发明人 | 文本 | F_IN:李书福 |
| `AT` | 代理人 | 文本 | AT:吴观乐 |
| `AT_C` | 当前代理人 | 文本 | AT_C:"GOUDREAU GAGE DUBUC" 仅支持受理局为CA的专利搜索 |
| `ATC` | 代理机构 | 文本 | ATC:柳沈 |
| `ATCS` | [标]代理机构 | 文本 | ATCS:柳沈 仅支持受理局为 CN 、 US 、 EP 、 WO 的专利搜索 |
| `ATCC` | 当前代理机构 | 文本 | ATCC:柳沈 仅支持受理局为CN的专利搜索 |
| `ATC_VALUE` | 委托代理机构专利 | 数字 | ATC_VALUE:1 0:无代理机构 1:具有代理机构 仅支持部分国家/地区专利 |
| `PE` | 审查员 | 文本 | PE:王剑 |
| `AE` | 助理审查员 | 文本 | AE:"SARTORI, MICHAEL A." 仅支持美国专利搜索 |
| `AUTHORITY` | 受理局 | 文本 | AUTHORITY:US |
| `PRIORITY_COUNTRY` | 优先权国家/地区 | 文本 | PRIORITY_COUNTRY:US |
| `EPDS` | EP指定国家/地区 | 文本 | EPDS:DE EP指定国家/地区是获取EP专利授权时的指定国家/地区，包含欧洲专利公约成员国即EPC成员国及EP专利延伸国/生效国。 EPDS:"DE"的检索结果包含检索到有DE指定国记录的已授权的EP专利和通过EP途径进入DE的DE专利。 EP指定国家/地区：阿尔巴尼亚(AL)，奥地利(AT)，比利时(BE)，保加利亚(BG)，瑞士(CH)，塞浦路斯(CY)，捷克(CZ)，德国(DE)，丹麦(DK)，爱沙尼亚(EE)，西班牙(ES)，芬兰(FI)，法国(FR)，英国(GB)，希腊(GR)，克罗地亚(HR)，匈牙利(HU)，冰岛(IS)，爱尔兰(IE)，意大利(IT)，列支敦士登(LI)，卢森堡(LU)，立陶宛(LT)，拉脱维亚(LV)，摩纳哥(MC)，黑山共和国(ME)，马其顿共和国(MK)，马耳他(MT)，荷兰(NL)，挪威(NO)，波兰(PL)，葡萄牙(PT)，罗马尼亚(RO)，塞尔维亚(RS)，瑞典(SE)，斯洛伐克(SK)，斯洛文尼亚(SI)，圣马力诺(SM)，土耳其(TR)，波斯尼亚和黑塞哥维那(BA)，摩洛哥(MA)，摩尔多瓦共和国(MD)，突尼斯(TN)，柬埔寨(KH), 南斯拉夫(YU)。 |
| `AN_EN` | 工商英文名 | 文本 | AN_EN:Xiaomi Technology 使用申请人的工商英文名称搜索 仅支持中国工商信息搜索 |
| `BI_USCC` | 工商统一社会信用代码 | 文本 | BI_USCC:914110007324785523 使用申请人在营业执照中的统一社会信用代码搜索 仅支持中国工商信息搜索 |
| `BI_RN` | 工商注册号 | 号码 | BI_RN:411000100003058 使用申请人在营业执照中的注册号搜索 仅支持中国工商信息搜索 |
| `BI_ADD` | 工商注册地址 | 文本 | BI_ADD:北京 使用申请人在营业执照中的住所搜索 仅支持中国工商信息搜索 |
| `BI_ET` | 工商企业类型 | 文本 | BI_ET:有限责任公司 使用申请人在营业执照中的类型搜索，例如有限责任公司、股份有限责任公司、个人独资企业、合伙企业等。 仅支持中国工商信息搜索 |
| `BI_ED` | 工商成立日期 | 号码 | BI_ED:20210101 使用申请人在营业执照中的成立日期搜索 仅支持中国工商信息搜索 |
| `BI_RS` | 工商登记状态 | 文本 | BI_RS:存续 使用申请人在营业执照中的登记状态搜索，例如存续、在业、吊销、注销、停业、清算等。 仅支持中国工商信息搜索 |
| `LC_CODE` | 工商上市公司代码 | 号码 | LC_CODE:002594 使用申请人的上市代码搜索 仅支持中国工商信息搜索 |

## 日期&分类

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `APD` | 申请日 | 日期 | APD:[* TO 20011231] APD:[20010101 TO *] APD:20010101 |
| `APD_Y` | 申请年 | 日期 | APD_Y:[* TO 2002] APD_Y:[2001 TO *] APD_Y:2001 |
| `APD_YM` | 申请年月 | 日期 | APD_YM:[* TO 200408] APD_YM:[200405 TO *] APD_YM:200405 |
| `PBD` | 公开日 | 日期 | PBD:[* TO 20011231] PBD:[20010101 TO *] PBD:20010101 |
| `F_PBD` | 首次公开日 | 日期 | F_PBD:[20150101 TO 20151231] F_PBD:20150101 |
| `PBD_Y` | 公开年 | 日期 | PBD_Y:[* TO 2012] PBD_Y:[2011 TO *] PBD_Y:2011 |
| `PBD_YM` | 公开年月 | 日期 | PBD_YM:[* TO 201405] PBD_YM:[201403 TO *] PBD_YM:201403 |
| `EFAM_EPBD` | 智慧芽同族最早公开日 | 日期 | EFAM_EPBD:[* TO 20231231] EFAM_EPBD:[20120101 TO *] EFAM_EPBD:20120101 |
| `EFAM_EPBY` | 智慧芽同族最早公开年 | 日期 | EFAM_EPBY:[* TO 2023] EFAM_EPBY:[2012 TO *] EFAM_EPBY:2012 |
| `EFAM_EPBYM` | 智慧芽同族最早公开年月 | 日期 | EFAM_EPBYM:[* TO 202312] EFAM_EPBYM:[201201 TO *] EFAM_EPBYM:201201 |
| `EFAM_EPRD` | 智慧芽同族最早优先权日 | 日期 | EFAM_EPRD:[* TO 20231231] EFAM_EPRD:[20120101 TO *] EFAM_EPRD:20120101 |
| `ISD` | 授权日 | 日期 | ISD:[* TO 20011231] ISD:[20010101 TO *] ISD:20010101 |
| `EXPD` | 失效日 | 日期 | EXPD:[20180101 TO 20181231] 仅支持部分国家/地区专利搜索 |
| `EXAMINE_DATE` | 实质审查生效日 | 日期 | EXAMINE_DATE:[20150101 TO 20151231] EXAMINE_DATE:20150101 仅支持部分国家/地区专利搜索 |
| `PCTENTRY_DATE` | PCT进入国家阶段日 | 日期 | PCTENTRY_DATE:[20010101 TO 20011231] PCTENTRY_DATE:20010101 |
| `LEGAL_STATUS_DATE` | 法律状态更新日 | 日期 | LEGAL_STATUS_DATE:[20150101 TO 20151231] LEGAL_STATUS_DATE:20150101 |
| `PRIORITY_DATE` | 优先权日 | 日期 | PRIORITY_DATE:[20010101 TO 20011231] PRIORITY_DATE:20010101 |
| `E_PRIORITY_DATE` | 最早优先权日 | 日期 | E_PRIORITY_DATE:[20010101 TO 20011231] |
| `EXDT` | 预估到期日 | 日期 | EXDT:[20160101 TO 20181231] |
| `CLASS` | 联合分类号 | 文本 | CLASS:A21B3/04 联合分类号：包括IPC分类，CPC分类，洛迦诺分类，FI分类，F-TERM分类，UPC分类 |
| `IPC` | IPC分类号 | 文本 | IPC:A61K IPC:[A21B3/04 TO A21B3/16] 支持分类号小组的范围检索，检索包含两个分类号之间的任一分类号的专利 |
| `IPC_SECTION` | IPC分类号部 | 文本 | IPC_SECTION:H |
| `IPC_CLASS` | IPC分类号大类 | 文本 | IPC_CLASS:H04 |
| `IPC_SUB_CLASS` | IPC分类号小类 | 文本 | IPC_SUB_CLASS:H04W |
| `IPC_GROUP` | IPC分类号大组 | 文本 | IPC_GROUP:A21B3 |
| `IPC_SUB_GROUP` | IPC分类号小组 | 文本 | IPC_SUB_GROUP:A21B3/04 |
| `MIPC` | IPC主分类号 | 文本 | MIPC:A61K MIPC:[A21B3/04 TO A21B3/16] 支持分类号小组的范围检索，检索包含两个分类号之间的任一分类号的专利 |
| `MIPC_SECTION` | IPC主分类号部 | 文本 | MIPC_SECTION:A |
| `MIPC_CLASS` | IPC主分类号大类 | 文本 | MIPC_CLASS:A61 |
| `MIPC_SUB_CLASS` | IPC主分类号小类 | 文本 | MIPC_SUB_CLASS:A61K |
| `IPC_CPC` | IPC/CPC | 文本 | IPC_CPC:B01B1/00 支持同时搜索IPC、CPC分类号 |
| `CPC` | CPC分类号 | 文本 | CPC:G10L15/193 CPC:[A21B3/04 TO A21B3/16] 支持分类号小组的范围检索，检索包含两个分类号之间的任一分类号的专利 |
| `CPC_ALL` | 官方/预测CPC分类号 | 文本 | CPC_ALL:G10L15/193 CPC_ALL:[A21B3/04 TO A21B3/16] 支持同时检索官方以及智慧芽预测的CPC分类号 |
| `CPC_SECTION` | CPC分类号部 | 文本 | CPC_SECTION:G |
| `CPC_CLASS` | CPC分类号大类 | 文本 | CPC_CLASS:G10 |
| `CPC_SUB_CLASS` | CPC分类号小类 | 文本 | CPC_SUB_CLASS:G10L |
| `CPC_GROUP` | CPC分类号大组 | 文本 | CPC_GROUP:G10L15 |
| `CPC_SUB_GROUP` | CPC分类号小组 | 文本 | CPC_SUB_GROUP:G10L15/193 |
| `MCPC` | CPC主分类号 | 文本 | MCPC:H02J7/007 MCPC:[A21B3/04 TO A21B3/16] 支持分类号小组的范围检索，检索包含两个分类号之间的任一分类号的专利 |
| `GBC` | 国民经济行业分类号 | 文本 | GBC:A0119 |
| `GBC_SECTION` | 国民经济行业分类门类 | 文本 | GBC_SECTION:A |
| `LOC` | LOC分类号 | 文本 | LOC:01-01 LOC:[04-01 TO 04-03] 仅支持外观专利搜索 支持分类号小类的范围检索，检索包含两个分类号之间的任一分类号的专利 |
| `UPC` | UPC分类号 | 文本 | UPC:530/388.2 仅支持美国专利搜索 |
| `FI` | FI分类号 | 文本 | FI:C12N5/00.A 仅支持日本专利搜索 |
| `FTERM` | F-TERM分类号 | 文本 | FTERM:4B024/HA11 仅支持日本专利搜索 |
| `IPC_LOW` | IPC分类号下位组 | 文本 | IPC_LOW:A01B1/02 仅在当前分类及其子分类中进行搜索 |
| `MIPC_LOW` | IPC主分类号下位组 | 文本 | MIPC_LOW:A01B1/02 仅在当前分类及其子分类中进行搜索 |
| `CPC_LOW` | CPC分类号下位组 | 文本 | CPC_LOW:A01B1/02 仅在当前分类及其子分类中进行搜索 |
| `UPC_LOW` | UPC分类号下位组 | 文本 | UPC_LOW:126/567 仅在当前分类及其子分类中进行搜索。仅支持美国专利搜索 |
| `FI_LOW` | FI分类号下位组 | 文本 | FI_LOW:A01B1/02 仅在当前分类及其子分类中进行搜索。仅支持日本专利搜索 |
| `FTERM_LOW` | F-TERM分类号下位组 | 文本 | FTERM_LOW:2B002/AA01 仅在当前分类及其子分类中进行搜索。仅支持日本专利搜索 |
| `ADC` | 应用领域分类 | 文本 | ADC:"发动机制造" |
| `TTC` | 技术主题分类 | 文本 | TTC:"麦克风" |
| `SEIC` | 战略新兴产业分类(主分类) | 文本 | SEIC:"人工智能" |
| `SEIC_ALL` | 战略新兴产业分类 | 文本 | SEIC_ALL:"人工智能" |

## 引用&同族

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `B_CITES` | 引用专利 | 号码 | B_CITES:US6394621B1 搜索指定专利引用的所有专利 |
| `F_CITES` | 被引用专利 | 号码 | F_CITES:US6394621B1 搜索指定专利被哪些专利引用 |
| `BF_CITES` | 引用或被引用专利 | 号码 | BF_CITES:US6394621B1 同时搜索指定专利引用的所有专利以及被哪些专利引用 |
| `B_CITES_COUNT` | 引用专利数量 | 数字 | B_CITES_COUNT:[10 TO 20] B_CITES_COUNT:10 搜索引用专利数在特定数量范围内的专利 |
| `F_CITES_COUNT` | 被引用专利数量 | 数字 | F_CITES_COUNT:[10 TO 20] F_CITES_COUNT:10 搜索被引用专利数在特定数量范围内的专利 |
| `F_CITES_ANC` | 引用当前申请人 | 文本 | F_CITES_ANC:清华大学 搜索所有引用清华大学的专利 |
| `B_CITES_ANC` | 当前申请人引用 | 文本 | B_CITES_ANC:清华大学 搜索所有被清华大学引用的专利 |
| `CITE_CATEGORY` | 引用类别 | 文本 | CITE_CATEGORY:X 搜索有指定引用类别的专利 文献类别： X：具有特别相关性，单独对比便可否定发明申请文件的新颖性或创造性的文献 Y：具有特别相关性，与其它类似文献结合，可否定发明申请创造性的文献，这种结合对于本领域技术人员是显而易见的 A：定义为一般现有技术水平文献，没有特别相关性 D：由申请人在申请中引证的文献 E：在先文献，但公布日在国际申请日的同时或之后（需要核实是否抵触申请） L：可能引起对优先权要求产生怀疑的文献，或者为了确定其他引证文献的公布日期或由于其他特殊原因而引证而引证的文献 R：任何单位或者个人在申请日向专利局提交、属同样的发明创造的专利或专利申请文件 T：在后文件公开晚于国际申请日或优先权日，不与申请文件相冲突，但引用有助于理解发明原理 101：搜索引用了101条款（保护客体）的美国专利申请 102：用于确定美国专利申请的新颖性的文献 103：用于确定美国专利申请的非显而易见性的文献 |
| `FAM` | 简单同族 | 号码 | FAM:WO2012001234A1 |
| `IFAM` | INPADOC同族 | 号码 | IFAM:WO2012001234A1 |
| `EFAM` | 智慧芽同族 | 号码 | EFAM:WO2012001234A1 |
| `FAM_COUNT` | 简单同族专利申请数量 | 数字 | FAM_COUNT:[10 TO 20] FAM_COUNT:10 一组简单同族下的专利申请件数搜索 |
| `IFAM_COUNT` | INPADOC同族专利申请数量 | 数字 | IFAM_COUNT:[10 TO 20] IFAM_COUNT:10 一组INPADOC同族下的专利申请件数搜索 |
| `EFAM_COUNT` | 智慧芽同族专利申请数量 | 数字 | EFAM_COUNT:[10 TO 20] EFAM_COUNT:10 一组智慧芽同族下的专利申请件数搜索 |
| `EFAM_COUNTRY` | 智慧芽同族国家/地区 | 文本 | EFAM_COUNTRY:CN 国家/地区代码搜索 |
| `EFAM_EPB_COUNTRY` | 智慧芽同族最早公开国家/地区 | 文本 | EFAM_EPB_COUNTRY:CN 国家/地区代码搜索 |
| `FAM_COUNTRY` | 简单同族国家/地区 | 文本 | FAM_COUNTRY:CN 国家/地区代码搜索 |
| `FAM_COUNTRY_COUNT` | 简单同族国家/地区数量 | 数字 | FAM_COUNTRY_COUNT:[1 TO 3] FAM_COUNTRY_COUNT:3 |
| `IFAM_COUNTRY_COUNT` | INPADOC同族国家/地区数量 | 数字 | IFAM_COUNTRY_COUNT:[1 TO 3] IFAM_COUNTRY_COUNT:3 |
| `EFAM_COUNTRY_COUNT` | 智慧芽同族国家/地区数量 | 数字 | EFAM_COUNTRY_COUNT:[1 TO 3] EFAM_COUNTRY_COUNT:3 |
| `EPDS_COUNT` | EP指定国家/地区数量 | 数字 | EPDS_COUNT:[1 TO 3] EPDS_COUNT:3 |

## 专利状态&质量

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `LEGAL_STATUS` | 法律状态 | 数字 | LEGAL_STATUS:3 1:公开 2:实质审查 3:授权 8:避免重复授权 11:撤回 12:撤回-未指定类型 17:撤回-视为撤回 18:撤回-主动撤回 13:驳回 14:全部撤销 15:期限届满 16:未缴年费 21:权利恢复 22:权利终止 23:部分无效 24:申请终止 30:放弃 19:放弃-视为放弃 20:放弃-主动放弃 25:放弃-未指定类型 222:PCT未进入指定国（指定期内） 223:PCT进入指定国（指定期内） 224:PCT进入指定国（指定期满） 225:PCT未进入指定国（指定期满） |
| `LEGAL_EVENT` | 法律事件 | 数字 | LEGAL_EVENT:61 61:权利转移 62:许可 63:质押 64:信托 65:异议 66:复审 69:海关备案 70:诉讼 71:保全 72:无效程序 73:口头审理 74:国防解密 75:一案双申 76:期限延长 |
| `SIMPLE_LEGAL_STATUS` | 简单法律状态 | 数字 | SIMPLE_LEGAL_STATUS:1 0:失效 1:有效 2:审中 220:PCT指定期满 221:PCT指定期内 999:未确认 |
| `EFAM_STATUS` | 智慧芽同族状态 | 数字 | EFAM_STATUS:1 0:失效 1:有效 2:审中 999:未确认 |
| `UP_STATUS` | 欧洲统一法院状态 | 数字 | UP_STATUS:1 0:未选择退出 1:选择退出 2:选择退出后撤回 3:UP专利已注册 |
| `ENTRY_COUNTRY_LS` | 进入国家/地区法律状态 | 数字 | ENTRY_COUNTRY_LS:3 1:公开 2:实质审查 3:授权 8:避免重复授权 11:撤回 12:撤回-未指定类型 17:撤回-视为撤回 18:撤回-主动撤回 13:驳回 14:全部撤销 15:期限届满 16:未缴年费 21:权利恢复 22:权利终止 23:部分无效 24:申请终止 30:放弃 19:放弃-视为放弃 20:放弃-主动放弃 25:放弃-未指定类型 |
| `ENTRY_COUNTRY_SLS` | 进入国家/地区简单法律状态 | 数字 | ENTRY_COUNTRY_SLS:1 0:失效 1:有效 2:审中 999:未确认 |
| `EPDS_LS` | EP指定国家/地区法律状态 | 数字 | EPDS_LS:3 3:授权 14:全部撤销 15:期限届满 16:未缴年费 21:权利恢复 22:权利终止 23:部分无效 30:放弃 19:放弃-视为放弃 20:放弃-主动放弃 25:放弃-未指定类型 EPDS_LS:"3"的检索结果包含指定国状态存在授权的EP专利和通过EP途径进入的状态为授权的国家专利。 放弃包含视为放弃和主动放弃，视为放弃包含因未能在规定时限内提交译文或支付费用而导致EP进入国家阶段未完成国家阶段生效手续的视为专利权的放弃；主动放弃是申请人主动提交文件表示放弃专利权。 授权为EP专利授权后在指定国已经生效，包含EP专利进入指定国已经符合授权要求处于有效，或者是EP专利授权后在指定的《伦敦协议》缔约国自动生效，待被指定国确认。 |
| `EPDS_SLS` | EP指定国家/地区简单法律状态 | 数字 | EPDS_SLS:1 0:失效 1:有效 999:未确认 有效包含EP专利在指定国已经符合授权要求处于有效，或者是EP专利授权后在指定的《伦敦协议》缔约国自动生效，待被指定国确认生效。 失效表示EP专利在指定国没有生效或生效后的失效，可能是由于保护期届满，放弃或撤回，未缴年费，被全部无效等任何一种原因导致失效。 未确认包含专利在这些非《伦敦协议》缔约国已经符合所有授权要求，但还没有信息确认在生效期限内已经缴纳费用和提交翻译，因此具体权利状况待定。 |
| `PV` | 专利价值 | 数字 | PV:[10000 TO 50000] PV:10000 |
| `PAGE_COUNT` | 文献页数 | 数字 | PAGE_COUNT:[5 TO 10] PAGE_COUNT:5 仅支持部分国家/地区专利搜索。文献页数是专利PDF页数。不支持外观专利搜索。 |
| `CLAIM_COUNT` | 权利要求数 | 数字 | CLAIM_COUNT:[10 TO 20] CLAIM_COUNT:10 |
| `FCLMS_WORDCOUNT` | 第一权利要求字数 | 数字 | FCLMS_WORDCOUNT:[100 TO 300] 仅支持原文是中英文的专利，中文按字计算，英文按单词计算 |
| `AN_COUNT` | 原始申请(专利权)人数量 | 数字 | AN_COUNT:[2 TO 3] AN_COUNT:2 |
| `ANC_COUNT` | 当前申请(专利权)人数量 | 数字 | ANC_COUNT:[2 TO 3] ANC_COUNT:2 |
| `IN_COUNT` | 发明人数量 | 数字 | IN_COUNT:[2 TO 3] IN_COUNT:2 |
| `CPC_COUNT` | CPC分类数量 | 数字 | CPC_COUNT:[2 TO 3] CPC_COUNT:2 |
| `IPC_COUNT` | IPC分类数量 | 数字 | IPC_COUNT:[2 TO 3] IPC_COUNT:2 |
| `GOV` | 政府利益 | 文本 | GOV:1 仅支持美国专利搜索 |
| `EXAMINE_PERIOD` | 审查时长 | 数字 | EXAMINE_PERIOD:[5 TO 10] EXAMINE_PERIOD:5 发明专利的实质审查生效日到授权公告日的时长，单位为月 仅支持部分国家/地区专利搜索 |
| `PATENT_TYPE` | 专利类型 | 文本 | PATENT_TYPE:D A: 发明申请 B: 授权发明 U: 实用新型 D: 外观设计 |
| `PCTENTRY_TYPE` | PCT路径进入专利 | 文本 | PCTENTRY_TYPE:1 检索结果包含有进入国信息的WO专利和通过PCT途径进入的具体国家专利 |
| `EP_ENTRY` | EPO路径进入专利 | 文本 | EP_ENTRY:1 检索结果包含有进入国信息的已授权的EP专利和通过EP途径进入的具体国家专利 |
| `ENTRY_COUNTRY` | 进入国家/地区 | 文本 | ENTRY_COUNTRY:DE 检索特定国家或地区已进入国家/地区阶段的专利。该字段包括基于EP生效国、PCT进入国家阶段和直接国家申请的数据。 |
| `SEP` | 所有标准专利 | 数字 | SEP:1 |
| `SEP_NUMBER` | 标准号 | 文本 | SEP_NUMBER:"TS 138 211" 仅支持搜索完整标准号 |
| `SEP_TITLE` | SEP标准标题 | 文本 | SEP_TITLE:E-UTRA 仅支持搜索英文 |
| `SEP_SOURCE` | SEP数据源 | 文本 | SEP_SOURCE:ETSI 数据源：ETSI/IEC/IEEE/ISO/ANSI/CEN/ITU |
| `SEP_PROJECT` | 标准-项目 | 文本 | SEP_PROJECT:5G 仅支持搜索英文 |
| `SEP_DECLARANT` | SEP标准持有者 | 文本 | SEP_DECLARANT:huawei 仅支持搜索英文 |
| `AWARD_NAME` | 奖励名称 | 文本 | AWARD_NAME:(中国专利奖) 仅支持受理局为CN和欧洲专利 |
| `AWARD_LEVEL` | 奖励等级 | 文本 | AWARD_LEVEL:(金奖) 仅支持受理局为CN的专利；仅支持搜索完整奖励等级 例如：一等奖、二等奖、三等奖、优秀奖、银奖、金奖、特等奖、外观设计优秀奖、外观设计金奖、外观设计银奖 |
| `AWARD_SESSION` | 奖励届次 | 文本 | AWARD_SESSION:(第一届) 仅支持受理局为CN和欧洲专利 |
| `SUB_CASE` | 分案 | 号码 | SUB_CASE:(US10/771529) 通过某个专利的申请号查看它的所有分案 |
| `PRIORITY_COUNTRY_COUNT` | 优先权国家/地区个数 | 数字 | PRIORITY_COUNTRY_COUNT:[10 TO 20] PRIORITY_COUNTRY_COUNT:10 |
| `PRIORITY_EMPTY` | 所有无优先权专利 | 数字 | PRIORITY_EMPTY:1 0:有优先权的专利 1:无优先权的专利 |

## 诉讼

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `LITIGATION` | 专利诉讼 | 数字 | LITIGATION:1 仅支持部分国家/地区专利搜索 |
| `CASENO` | 案件号 | 文本 | CASENO:("(2012)浙杭知初字第425号") 仅支持部分国家/地区专利搜索 |
| `COURT` | 审理法院 | 文本 | COURT:(浙江省杭州市中级人民法院) 仅支持部分国家/地区专利搜索 |
| `JUDGE` | 审判员 | 文本 | JUDGE:(王江桥) 仅支持部分国家/地区专利搜索 |
| `CHIEF_JUDGE` | 审判长 | 文本 | CHIEF_JUDGE:张艳培 仅支持部分国家/地区专利搜索 |
| `PLAINTIFF` | 原告 | 文本 | PLAINTIFF:(华为) 仅支持部分国家/地区专利搜索 |
| `DEFENDANT` | 被告 | 文本 | DEFENDANT:(中兴) 仅支持部分国家/地区专利搜索 |
| `FILING_DATE` | 立案日期 | 日期 | FILING_DATE:[20150101 TO 20150630] 仅支持部分国家/地区专利搜索 |
| `VERDICT_DATE` | 裁判日期 | 日期 | VERDICT_DATE:[20150101 TO 20151231] 仅支持部分国家/地区专利搜索 |
| `HEARING_DATE` | 听证日期 | 日期 | HEARING_DATE:[20150101 TO 20151231] 仅支持部分国家/地区专利搜索 |
| `TRIAL_GRADE` | 审理程序 | 文本 | TRIAL_GRADE:(一审) 仅支持部分国家/地区专利搜索 |
| `CASE_NATURE` | 案件性质 | 文本 | CASE_NATURE:(民事案件) 仅支持部分国家/地区专利搜索 |
| `CASE_LEVEL` | 案例级别 | 文本 | CASE_LEVEL:(1) 仅支持受理局为CN的专利搜索 1：典型案例 2：普通案例 |
| `CASE_REGION` | 审理地域 | 文本 | CASE_REGION:(江苏) 仅支持部分国家/地区专利搜索 |
| `CASE_TITLE` | 案件标题 | 文本 | CASE_TITLE:(华为) 仅支持部分国家/地区专利搜索 |
| `CASE_FULL_TEXT` | 案件全文 | 文本 | CASE_FULL_TEXT:(照明) 仅支持部分国家/地区专利搜索 |
| `LIT_CLOSEDT` | 结案日期 | 日期 | LIT_CLOSEDT:[20150101 TO 20151231] 仅支持部分国家/地区专利搜索 |
| `OUTCOME_JUDGEMENT` | 胜诉方 | 文本 | OUTCOME_JUDGEMENT:(原告) |
| `OUTCOME_STATUS` | 案件状态 | 文本 | OUTCOME_STATUS:("Closed (closed)") 仅支持部分国家/地区专利搜索 |
| `LITIGATION_COUNT` | 诉讼次数 | 数字 | LITIGATION_COUNT:2 仅支持部分国家/地区专利搜索 |
| `CASE_DOC_TYPE` | 文书类型 | 文本 | CASE_DOC_TYPE:2 仅支持受理局为CN的专利搜索 1:判决书 2:裁定书 3:调解书 4:决定书 5:其他文书 |
| `COURT_GRADE` | 法院级别 | 文本 | COURT_GRADE:中级法院 仅支持受理局为CN的专利搜索 例如：最高法院、高级法院、中级法院、基层法院、专门法院 |
| `VERDICT` | 判决结果 | 文本 | VERDICT:(驳回) 暂不支持US专利搜索 |
| `PARTY` | 当事人 | 文本 | PARTY:(华为) 当事人包括原告、被告及第三方当事人数据 仅支持部分国家/地区专利搜索 |
| `PARTY_AGENT` | 当事人委托代理人 | 文本 | PARTY_AGENT:(王佩佩) 当事人委托代理人包括原告代理人、被告代理人及第三方当事人代理人数据 仅支持部分国家/地区专利搜索 |
| `PARTY_LAWFIRM` | 当事人委托律所 | 文本 | PARTY_LAWFIRM:(广东非凡律师事务所) 仅支持部分国家/地区专利搜索 |
| `AMOUNT_PLAINTIFF` | 申请赔偿总额 | 数字 | AMOUNT_PLAINTIFF:[10000 TO 50000] 仅支持受理局为CN的专利搜索 |
| `DAMAGES_AMOUNT` | 判赔总额 | 数字 | DAMAGES_AMOUNT:[10000 TO 50000] 仅支持受理局为CN的专利搜索 |
| `FILING_YEAR` | 立案年份 | 日期 | FILING_YEAR:[2011 TO 2012] 仅支持部分国家/地区专利搜索 |
| `LITIGATION_PRODUCT` | 涉及产品 | 文本 | LITIGATION_PRODUCT:(真空运动瓶) 仅支持部分国家/地区专利搜索 |

## 许可

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `LICENSE` | 所有发生许可的专利 | 数字 | LICENSE:1 |
| `LICENSOR` | 许可人 | 文本 | LICENSOR:(三星) 仅支持部分国家/地区专利搜索 |
| `LICENSEE` | 被许可人 | 文本 | LICENSEE:(小米) 仅支持部分国家/地区专利搜索 |
| `LICNO` | 许可合同备案号 | 文本 | LICNO:2014510000101 仅支持部分国家/地区专利搜索 |
| `EXCLUSIVITY` | 许可排他性 | 文本 | EXCLUSIVITY:(Exclusive) 仅支持部分国家/地区专利搜索 |
| `LIC_EFDT` | 许可生效日 | 日期 | LIC_EFDT:[20160101 TO 20160501] 仅支持部分国家/地区专利搜索 |
| `LICENSE_COUNT` | 许可次数 | 数字 | LICENSE_COUNT:2 |

## 权利转移

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `TRANSFER` | 所有发生转让的专利 | 数字 | TRANSFER:1 |
| `TRANSFER_BEFORE` | 转让人 | 文本 | TRANSFER_BEFORE:(英特尔) 仅支持部分国家/地区专利搜索 |
| `TRANSFER_AFTER` | 受让人 | 文本 | TRANSFER_AFTER:(华为) 仅支持部分国家/地区专利搜索 |
| `TRANS_EFDT` | 权利转移生效日 | 日期 | TRANS_EFDT:[20180701 TO 20181231] 仅支持部分国家/地区专利搜索 |

## 复审无效

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `REEXAMINVALID` | 所有发生复审/无效的专利 | 数字 | REEXAMINVALID:1 仅支持部分国家/地区专利搜索 |
| `RI_APPLICANT` | 复审/无效请求人 | 文本 | RI_APPLICANT:彭宇轴 仅支持部分国家/地区专利搜索 |
| `RIDN` | 决定号 | 文本 | RIDN:(FS1112) 仅支持部分国家/地区专利搜索 |
| `RIIN` | 委内编号 | 文本 | RIIN:(F12964) 仅支持部分国家/地区专利搜索 |
| `RIDDT` | 决定/发文日 | 日期 | RIDDT:[20160101 TO 20160501] 仅支持部分国家/地区专利搜索 |
| `RIDTP` | 决定类型 | 文本 | RIDTP:(FS) 仅支持部分国家/地区专利搜索 |
| `RID` | 决定 | 文本 | RID:(全部无效) 仅支持部分国家/地区专利搜索 |
| `RIDP` | 决定要点 | 文本 | RIDP:(技术方案) 仅支持部分国家/地区专利搜索 |
| `RIDSM` | 案由 | 文本 | RIDSM:(不符合专利法第22条第3款的规定) 仅支持部分国家/地区专利搜索 |
| `RILGS` | 法律依据 | 文本 | RILGS:(专利法第22条第3款) 仅支持部分国家/地区专利搜索 |
| `RI_FULL_TEXT` | 复审/无效全文 | 文本 | RI_FULL_TEXT:(技术问题) 仅支持受理局为CN的专利搜索 |
| `INVALID_COUNT` | 无效次数 | 数字 | INVALID_COUNT:2 仅支持部分国家/地区专利搜索 |

## 质押

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `PLEDGE` | 专利质押 | 数字 | PLEDGE:1 |
| `PLEDGOR` | 质押人 | 文本 | PLEDGOR:auto 仅支持受理局为CN的质押、美国担保专利搜索 |
| `PLEDGEE` | 质权人 | 文本 | PLEDGEE:(SILICON VALLEY BANK) 仅支持受理局为CN的质押、美国担保专利搜索 |
| `PLEDGENO` | 质押登记号 | 文本 | PLEDGENO:2015990000410 仅支持受理局为CN的质押、美国担保专利搜索 |
| `PLE_EFDT` | 质押生效日 | 日期 | PLE_EFDT:[20160101 TO 20160501] 仅支持受理局为CN的质押、美国担保专利搜索 |
| `PLE_STAGE` | 质押备案阶段 | 文本 | PLE_STAGE:1 仅支持受理局为CN的专利搜索 |
| `PLEDGE_COUNT` | 质押次数 | 数字 | PLEDGE_COUNT:2 |

## 工作空间

| 字段缩写 | 字段名称 | 类型 | 示例和备注 |
| --- | --- | --- | --- |
| `MWS` | 我的工作空间 | 文本 | MWS:\|工作空间A\文件夹B\| 仅支持对于我的工作空间下的文件夹搜索，请将文件夹路径放在\|\|内 |
| `CWS` | 企业工作空间 | 文本 | CWS:\|工作空间A\文件夹B\| 仅支持对于企业工作空间下的文件夹搜索，请将文件夹路径放在\|\|内 |
| `CCF_` | 企业自定义字段 | 文本 | CCF_PR:"标引值A" 请将层级字段、选项字段的标引值放在""内 对于链接URL类型的字段，"not blank"表示该字段下有值 |
