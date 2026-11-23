# Patsnap Searchable Fields

> Use these fields and syntax to construct queries; actual calls must follow the tool schema. Mark unexecuted syntax as pending validation. See [Tool usage](tool-usage.md).

Source: `智慧芽可搜索字段.docx`, parsed into a reusable field reference for the skill.

Total fields identified: 269.

Use this file when the user asks for a Patsnap/Zhihuiya executable search formula or when mapping a retrieval idea to exact searchable fields. Prefer the source document if the user provides an updated version.

## Category Summary

| Category | Field count |
| --- | ---: |
| Numbers and text | 47 |
| Companies and people | 47 |
| Dates and classifications | 55 |
| Citations and families | 21 |
| Patent status and quality | 36 |
| Litigation | 30 |
| Licensing | 7 |
| Transfers | 4 |
| Reexamination and invalidation | 12 |
| Pledges | 7 |
| Workspaces | 3 |

## Numbers and text

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `PN` | Publication number | Identifier | PN:US1234567 |
| `APNO` | Application number | Identifier | APNO:US10/123456 |
| `PRNO` | Priority number | Identifier | PRNO:JP2013270967 |
| `KD` | Kind code | Identifier | KD:B1 |
| `PCT_PN` | PCT international publication number | Identifier | PCT_PN:WO2017161368 |
| `PCT_APNO` | PCT international application number | Identifier | PCT_APNO:US2017/023191 |
| `FAM_ID` | Simple family ID | Identifier | FAM_ID:138860071 |
| `IFAM_ID` | INPADOC family ID | Identifier | IFAM_ID:438860071 |
| `EFAM_ID` | Patsnap family ID | Identifier | EFAM_ID:742326667 |
| `TTL` | Title | Text | TTL:汽车 |
| `ABST` | Abstract | Text | ABST:汽车 |
| `CLMS` | Claims | Text | CLMS:汽车 |
| `ICLMS` | Independent claims | Text | ICLMS:car Supports English-language patents and CN patents only. |
| `DESC` | Description | Text | DESC:汽车 |
| `DESC_F` | Technical field | Text | DESC_F:汽车 Supports CN patents only. |
| `DESC_B` | Background | Text | DESC_B:汽车 Supports CN patents only. |
| `DESC_S` | Summary of the invention | Text | DESC_S:汽车 Supports CN patents only. |
| `DESC_D` | Description of drawings | Text | DESC_D:汽车 Supports CN patents only. |
| `DESC_E` | Detailed embodiments | Text | DESC_E:汽车 Supports CN patents only. |
| `PROBLEM_SUM` | Technical problem | Text | PROBLEM_SUM:透气性差 Supports worldwide patents with description text. |
| `METHOD_SUM` | Technical means | Text | METHOD_SUM:汽车 Supports worldwide patents with description text. |
| `BENEFIT_SUM` | Technical effect | Text | BENEFIT_SUM:汽车 Supports worldwide patents with description text. |
| `PROBLEM_PHR` | Standardized technical problem phrase | Text | PROBLEM_PHR:成本高 Supports CN/US/EP/WO patents only. |
| `BENEFIT_PHR` | Standardized technical effect phrase | Text | BENEFIT_PHR:降低成本 Supports CN/US/EP/WO patents only. |
| `TA` | Title / abstract | Text | TA:(汽车 and 座椅) |
| `TAC` | Title / abstract / claims | Text | TAC:(汽车 and 座椅) |
| `TACD` | Title / abstract / claims / description | Text | TACD:(汽车 and 座椅) |
| `MAINF` | Main fields | Text | MAINF:汽车 Main fields include title, abstract, claims, description, publication/application numbers, applicants, inventors, and IPC/UPC/LOC classifications. Queries without a field use these main fields by default. |
| `TTL_ENTRANS` | Title — English machine translation | Text | TTL_ENTRANS:car |
| `ABST_ENTRANS` | Abstract — English machine translation | Text | ABST_ENTRANS:car |
| `CLMS_ENTRANS` | Claims — English machine translation | Text | CLMS_ENTRANS:car |
| `ICLMS_ENTRANS` | Independent claims — English machine translation | Text | ICLMS_ENTRANS:car |
| `DESC_ENTRANS` | Description — English machine translation | Text | DESC_ENTRANS:car |
| `TTL_CNTRANS` | Title — Chinese machine translation | Text | TTL_CNTRANS:汽车 |
| `ABST_CNTRANS` | Abstract — Chinese machine translation | Text | ABST_CNTRANS:汽车 |
| `CLMS_CNTRANS` | Claims — Chinese machine translation | Text | CLMS_CNTRANS:汽车 |
| `ICLMS_CNTRANS` | Independent claims — Chinese machine translation | Text | ICLMS_CNTRANS:汽车 |
| `DESC_CNTRANS` | Description — Chinese machine translation | Text | DESC_CNTRANS:汽车 |
| `TTL_ALL` | Title — original and translated text | Text | TTL_ALL:汽车 |
| `ABST_ALL` | Abstract — original and translated text | Text | ABST_ALL:汽车 |
| `CLMS_ALL` | Claims — original and translated text | Text | CLMS_ALL:汽车 |
| `ICLMS_ALL` | Independent claims — original and translated text | Text | ICLMS_ALL:汽车 |
| `DESC_ALL` | Description — original and translated text | Text | DESC_ALL:汽车 |
| `TA_ALL` | Title / abstract — original and translated text | Text | TA_ALL:汽车 |
| `TAC_ALL` | Title / abstract / claims — original and translated text | Text | TAC_ALL:汽车 |
| `TACD_ALL` | Title / abstract / claims / description — original and translated text | Text | TACD_ALL:汽车 |
| `MAINF_ALL` | Main fields — original and translated text | Text | MAINF_ALL:汽车 Includes original and translated title, abstract, claims and description, plus publication/application numbers, applicants, inventors and IPC/UPC/LOC classifications. |

## Companies and people

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `ALL_AN` | Applicant/assignee across all fields | Text | ALL_AN:清华大学 Combined index of standardized current, current, standardized original, original and historical applicants/assignees. |
| `AN` | Original applicant/assignee | Text | AN:清华大学 The initial applicant/assignee. |
| `ANC` | Current applicant/assignee | Text | ANC:清华大学 The current applicant/assignee. |
| `ANS` | Standardized original applicant/assignee | Text | ANS:清华大学 Initial applicant/assignee standardized by Patsnap. |
| `ANS_EXACT` | Exact standardized original applicant/assignee | Text | ANS_EXACT:清华大学 Exact match of standardized original applicant/assignee, including symbols and case. |
| `ANCS` | Standardized current applicant/assignee | Text | ANCS:清华大学 Current applicant/assignee standardized by Patsnap. |
| `ANCS_EXACT` | Exact standardized current applicant/assignee | Text | ANCS_EXACT:清华大学 Exact match of standardized current applicant/assignee, including symbols and case. |
| `AN_HIST` | Historical applicant/assignee | Text | AN_HIST:清华大学 Includes applicants/assignees recorded during transfers, changes, pledges and security interests. |
| `GNAME` | Custom applicant group | Text | GNAME:清华大学 |
| `AN_ADD` | Original applicant/assignee address | Text | AN_ADD:北京 |
| `AN_COUNTRY` | Original applicant/assignee country or region | Text | AN_COUNTRY:CN AN_COUNTRY:中国 Search by applicant country/region name or code. |
| `AN_PROVINCE` | Original applicant/assignee state or province | Text | AN_PROVINCE:江苏 AN_PROVINCE:32 Search by province name or code. Supports CN patents only. |
| `AN_CITY` | Original applicant/assignee city | Text | AN_CITY:南京 Search by Chinese city or US municipality. Supports CN and US patents only. |
| `AN_DISTRICT` | Original applicant/assignee district or county | Text | AN_DISTRICT:鼓楼区 Search by Chinese district/county or US county. Supports CN and US patents only. |
| `ANC_ADD` | Current applicant/assignee address | Text | ANC_ADD:北京 |
| `ANC_COUNTRY` | Current applicant/assignee country or region | Text | ANC_COUNTRY:CN ANC_COUNTRY:中国 Search by applicant country/region name or code. |
| `ANC_PROVINCE` | Current applicant/assignee state or province | Text | ANC_PROVINCE:江苏 ANC_PROVINCE:32 Search by province name or code. Supports CN patents only. |
| `ANC_CITY` | Current applicant/assignee city | Text | ANC_CITY:南京 Search by Chinese city or US municipality. Supports CN and US patents only. |
| `ANC_DISTRICT` | Current applicant/assignee district or county | Text | ANC_DISTRICT:鼓楼区 Search by Chinese district/county or US county. Supports CN and US patents only. |
| `F_AN` | First original applicant/assignee | Text | F_AN:清华大学 |
| `F_ANC` | First current applicant/assignee | Text | F_ANC:清华大学 |
| `ANS_TYPE` | Standardized original applicant/assignee type | Text | ANS_TYPE:ACADEMY ACADEMY: university/research institute; COMPANY: company; GOVERNMENT: government agency; PERSON: individual; HOSPITAL: hospital; BANK: bank. |
| `ANCS_TYPE` | Standardized current applicant/assignee type | Text | ANCS_TYPE:ACADEMY ACADEMY: university/research institute; COMPANY: company; GOVERNMENT: government agency; PERSON: individual; HOSPITAL: hospital; BANK: bank. |
| `IN` | Inventor | Text | IN:李书福 |
| `INC` | Current inventor | Text | INC:李书福 Current inventor name after a recorded change. Supports CN patents only. |
| `IN_EXACT` | Exact inventor | Text | IN_EXACT:李书福 Exact inventor match including symbols and case. |
| `IN_ADDRESS` | Inventor address | Text | IN_ADDRESS:北京 |
| `F_IN` | First inventor | Text | F_IN:李书福 |
| `AT` | Agent | Text | AT:吴观乐 |
| `AT_C` | Current agent | Text | AT_C:"GOUDREAU GAGE DUBUC" Supports CA patents only. |
| `ATC` | Agency | Text | ATC:柳沈 |
| `ATCS` | Standardized agency | Text | ATCS:柳沈 Supports CN/US/EP/WO patents only. |
| `ATCC` | Current agency | Text | ATCC:柳沈 Supports CN patents only. |
| `ATC_VALUE` | Patents with an agency | Number | ATC_VALUE:1 0: no agency; 1: has an agency. Available for selected countries/regions only. |
| `PE` | Examiner | Text | PE:王剑 |
| `AE` | Assistant examiner | Text | AE:"SARTORI, MICHAEL A." Supports US patents only. |
| `AUTHORITY` | Patent office | Text | AUTHORITY:US |
| `PRIORITY_COUNTRY` | Priority country/region | Text | PRIORITY_COUNTRY:US |
| `EPDS` | EP designated country/region | Text | EPDS:DE Designated countries/regions at EP grant, including EPC members and extension/validation states. EPDS:"DE" includes granted EP records designating DE and DE patents entering via the EP route. Source-listed codes: AL, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IS, IE, IT, LI, LU, LT, LV, MC, ME, MK, MT, NL, NO, PL, PT, RO, RS, SE, SK, SI, SM, TR, BA, MA, MD, TN, KH, YU. This is the source reference list, not a current membership assertion. |
| `AN_EN` | Registered English business name | Text | AN_EN:Xiaomi Technology Search the registered English business name. Chinese business registration data only. |
| `BI_USCC` | Unified social credit code | Text | BI_USCC:914110007324785523 Search the unified social credit code on the business license. Chinese business registration data only. |
| `BI_RN` | Business registration number | Identifier | BI_RN:411000100003058 Search the registration number on the business license. Chinese business registration data only. |
| `BI_ADD` | Registered business address | Text | BI_ADD:北京 Search the address on the business license. Chinese business registration data only. |
| `BI_ET` | Business entity type | Text | BI_ET:有限责任公司 Search the business-license entity type, such as limited liability company, joint-stock company, sole proprietorship or partnership. Chinese business registration data only. |
| `BI_ED` | Business establishment date | Identifier | BI_ED:20210101 Search the establishment date on the business license. Chinese business registration data only. |
| `BI_RS` | Business registration status | Text | BI_RS:存续 Search the business-license registration status, such as existing, operating, revoked, deregistered, suspended or in liquidation. Chinese business registration data only. |
| `LC_CODE` | Listed company stock code | Identifier | LC_CODE:002594 Search the stock listing code. Chinese business registration data only. |

## Dates and classifications

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `APD` | Application date | Date | APD:[* TO 20011231] APD:[20010101 TO *] APD:20010101 |
| `APD_Y` | Application year | Date | APD_Y:[* TO 2002] APD_Y:[2001 TO *] APD_Y:2001 |
| `APD_YM` | Application year and month | Date | APD_YM:[* TO 200408] APD_YM:[200405 TO *] APD_YM:200405 |
| `PBD` | Publication date | Date | PBD:[* TO 20011231] PBD:[20010101 TO *] PBD:20010101 |
| `F_PBD` | First publication date | Date | F_PBD:[20150101 TO 20151231] F_PBD:20150101 |
| `PBD_Y` | Publication year | Date | PBD_Y:[* TO 2012] PBD_Y:[2011 TO *] PBD_Y:2011 |
| `PBD_YM` | Publication year and month | Date | PBD_YM:[* TO 201405] PBD_YM:[201403 TO *] PBD_YM:201403 |
| `EFAM_EPBD` | Patsnap family earliest publication date | Date | EFAM_EPBD:[* TO 20231231] EFAM_EPBD:[20120101 TO *] EFAM_EPBD:20120101 |
| `EFAM_EPBY` | Patsnap family earliest publication year | Date | EFAM_EPBY:[* TO 2023] EFAM_EPBY:[2012 TO *] EFAM_EPBY:2012 |
| `EFAM_EPBYM` | Patsnap family earliest publication year and month | Date | EFAM_EPBYM:[* TO 202312] EFAM_EPBYM:[201201 TO *] EFAM_EPBYM:201201 |
| `EFAM_EPRD` | Patsnap family earliest priority date | Date | EFAM_EPRD:[* TO 20231231] EFAM_EPRD:[20120101 TO *] EFAM_EPRD:20120101 |
| `ISD` | Grant date | Date | ISD:[* TO 20011231] ISD:[20010101 TO *] ISD:20010101 |
| `EXPD` | Lapse date | Date | EXPD:[20180101 TO 20181231] Available for selected countries/regions only. |
| `EXAMINE_DATE` | Substantive examination effective date | Date | EXAMINE_DATE:[20150101 TO 20151231] EXAMINE_DATE:20150101 Available for selected countries/regions only. |
| `PCTENTRY_DATE` | PCT national phase entry date | Date | PCTENTRY_DATE:[20010101 TO 20011231] PCTENTRY_DATE:20010101 |
| `LEGAL_STATUS_DATE` | Legal status update date | Date | LEGAL_STATUS_DATE:[20150101 TO 20151231] LEGAL_STATUS_DATE:20150101 |
| `PRIORITY_DATE` | Priority date | Date | PRIORITY_DATE:[20010101 TO 20011231] PRIORITY_DATE:20010101 |
| `E_PRIORITY_DATE` | Earliest priority date | Date | E_PRIORITY_DATE:[20010101 TO 20011231] |
| `EXDT` | Estimated expiry date | Date | EXDT:[20160101 TO 20181231] |
| `CLASS` | Combined classifications | Text | CLASS:A21B3/04 Combined IPC, CPC, Locarno, FI, F-TERM and UPC classifications. |
| `IPC` | IPC classification | Text | IPC:A61K IPC:[A21B3/04 TO A21B3/16] Supports subgroup ranges; retrieves patents containing a classification between the two endpoints. |
| `IPC_SECTION` | IPC section | Text | IPC_SECTION:H |
| `IPC_CLASS` | IPC class | Text | IPC_CLASS:H04 |
| `IPC_SUB_CLASS` | IPC subclass | Text | IPC_SUB_CLASS:H04W |
| `IPC_GROUP` | IPC main group | Text | IPC_GROUP:A21B3 |
| `IPC_SUB_GROUP` | IPC subgroup | Text | IPC_SUB_GROUP:A21B3/04 |
| `MIPC` | Main IPC classification | Text | MIPC:A61K MIPC:[A21B3/04 TO A21B3/16] Supports subgroup ranges; retrieves patents containing a classification between the two endpoints. |
| `MIPC_SECTION` | MIPC section | Text | MIPC_SECTION:A |
| `MIPC_CLASS` | MIPC class | Text | MIPC_CLASS:A61 |
| `MIPC_SUB_CLASS` | MIPC subclass | Text | MIPC_SUB_CLASS:A61K |
| `IPC_CPC` | IPC/CPC | Text | IPC_CPC:B01B1/00 Searches IPC and CPC together. |
| `CPC` | CPC classification | Text | CPC:G10L15/193 CPC:[A21B3/04 TO A21B3/16] Supports subgroup ranges; retrieves patents containing a classification between the two endpoints. |
| `CPC_ALL` | Official / predicted CPC classification | Text | CPC_ALL:G10L15/193 CPC_ALL:[A21B3/04 TO A21B3/16] Searches official and Patsnap-predicted CPC classifications together. |
| `CPC_SECTION` | CPC section | Text | CPC_SECTION:G |
| `CPC_CLASS` | CPC class | Text | CPC_CLASS:G10 |
| `CPC_SUB_CLASS` | CPC subclass | Text | CPC_SUB_CLASS:G10L |
| `CPC_GROUP` | CPC main group | Text | CPC_GROUP:G10L15 |
| `CPC_SUB_GROUP` | CPC subgroup | Text | CPC_SUB_GROUP:G10L15/193 |
| `MCPC` | Main CPC classification | Text | MCPC:H02J7/007 MCPC:[A21B3/04 TO A21B3/16] Supports subgroup ranges; retrieves patents containing a classification between the two endpoints. |
| `GBC` | National economic industry classification | Text | GBC:A0119 |
| `GBC_SECTION` | National economic industry section | Text | GBC_SECTION:A |
| `LOC` | Locarno classification | Text | LOC:01-01 LOC:[04-01 TO 04-03] Design patents only. Supports subclass ranges between the two endpoints. |
| `UPC` | US classification | Text | UPC:530/388.2 Supports US patents only. |
| `FI` | FI classification | Text | FI:C12N5/00.A Supports JP patents only. |
| `FTERM` | F-TERM classification | Text | FTERM:4B024/HA11 Supports JP patents only. |
| `IPC_LOW` | IPC current class and descendants | Text | IPC_LOW:A01B1/02 Searches the current class and its descendants only. |
| `MIPC_LOW` | MIPC current class and descendants | Text | MIPC_LOW:A01B1/02 Searches the current class and its descendants only. |
| `CPC_LOW` | CPC current class and descendants | Text | CPC_LOW:A01B1/02 Searches the current class and its descendants only. |
| `UPC_LOW` | UPC current class and descendants | Text | UPC_LOW:126/567 Searches the current class and its descendants only.。Supports US patents only. |
| `FI_LOW` | FI current class and descendants | Text | FI_LOW:A01B1/02 Searches the current class and its descendants only.。Supports JP patents only. |
| `FTERM_LOW` | FTERM current class and descendants | Text | FTERM_LOW:2B002/AA01 Searches the current class and its descendants only.。Supports JP patents only. |
| `ADC` | Application area classification | Text | ADC:"发动机制造" |
| `TTC` | Technology topic classification | Text | TTC:"麦克风" |
| `SEIC` | Strategic emerging industry (main classification) | Text | SEIC:"人工智能" |
| `SEIC_ALL` | Strategic emerging industry classification | Text | SEIC_ALL:"人工智能" |

## Citations and families

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `B_CITES` | Backward citations | Identifier | B_CITES:US6394621B1 Retrieves patents cited by the specified patent. |
| `F_CITES` | Forward citations | Identifier | F_CITES:US6394621B1 Retrieves patents citing the specified patent. |
| `BF_CITES` | Backward or forward citations | Identifier | BF_CITES:US6394621B1 Retrieves both backward and forward citations of the specified patent. |
| `B_CITES_COUNT` | Backward citation count | Number | B_CITES_COUNT:[10 TO 20] B_CITES_COUNT:10 Searches patents by backward citation count range. |
| `F_CITES_COUNT` | Forward citation count | Number | F_CITES_COUNT:[10 TO 20] F_CITES_COUNT:10 Searches patents by forward citation count range. |
| `F_CITES_ANC` | Citing a current applicant | Text | F_CITES_ANC:清华大学 Retrieves patents citing Tsinghua University patents. |
| `B_CITES_ANC` | Cited by a current applicant | Text | B_CITES_ANC:清华大学 Retrieves patents cited by Tsinghua University patents. |
| `CITE_CATEGORY` | Citation category | Text | CITE_CATEGORY:X Searches patents with a specified citation category. X: particularly relevant, may negate novelty/inventive step alone; Y: particularly relevant in an obvious combination with another document; A: general prior art without special relevance; D: cited by the applicant; E: earlier document published on/after the international filing date (check conflicting-application eligibility); L: raises priority doubts, establishes another citation’s publication date or is cited for another special reason; R: same-invention patent/application submitted to the office on the filing date; T: later document explaining principles without conflicting with the application; 101: US subject-matter eligibility; 102: US novelty; 103: US non-obviousness. |
| `FAM` | Simple family | Identifier | FAM:WO2012001234A1 |
| `IFAM` | INPADOC family | Identifier | IFAM:WO2012001234A1 |
| `EFAM` | Patsnap family | Identifier | EFAM:WO2012001234A1 |
| `FAM_COUNT` | Applications in a simple family | Number | FAM_COUNT:[10 TO 20] FAM_COUNT:10 Searches the application count within a simple family. |
| `IFAM_COUNT` | Applications in an INPADOC family | Number | IFAM_COUNT:[10 TO 20] IFAM_COUNT:10 Searches the application count within an INPADOC family. |
| `EFAM_COUNT` | Applications in a Patsnap family | Number | EFAM_COUNT:[10 TO 20] EFAM_COUNT:10 Searches the application count within a Patsnap family. |
| `EFAM_COUNTRY` | Patsnap family country/region | Text | EFAM_COUNTRY:CN Search by country/region code. |
| `EFAM_EPB_COUNTRY` | Patsnap family earliest publication country/region | Text | EFAM_EPB_COUNTRY:CN Search by country/region code. |
| `FAM_COUNTRY` | Simple family country/region | Text | FAM_COUNTRY:CN Search by country/region code. |
| `FAM_COUNTRY_COUNT` | Simple family country/region count | Number | FAM_COUNTRY_COUNT:[1 TO 3] FAM_COUNTRY_COUNT:3 |
| `IFAM_COUNTRY_COUNT` | INPADOC family country/region count | Number | IFAM_COUNTRY_COUNT:[1 TO 3] IFAM_COUNTRY_COUNT:3 |
| `EFAM_COUNTRY_COUNT` | Patsnap family country/region count | Number | EFAM_COUNTRY_COUNT:[1 TO 3] EFAM_COUNTRY_COUNT:3 |
| `EPDS_COUNT` | EP designated country/region count | Number | EPDS_COUNT:[1 TO 3] EPDS_COUNT:3 |

## Patent status and quality

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `LEGAL_STATUS` | Legal status | Number | LEGAL_STATUS:3 1: published; 2: substantive examination; 3: granted; 8: prevention of double patenting; 11: withdrawn; 12: withdrawal, unspecified; 17: deemed withdrawn; 18: voluntarily withdrawn; 13: rejected; 14: fully revoked; 15: term expired; 16: unpaid renewal fee; 21: rights restored; 22: rights terminated; 23: partially invalidated; 24: application terminated; 30: abandoned; 19: deemed abandoned; 20: voluntarily abandoned; 25: abandonment, unspecified. 222: PCT not entered, designation period open; 223: PCT entered, period open; 224: PCT entered, period ended; 225: PCT not entered, period ended. |
| `LEGAL_EVENT` | Legal event | Number | LEGAL_EVENT:61 61: transfer; 62: licensing; 63: pledge; 64: trust; 65: opposition; 66: reexamination; 69: customs record; 70: litigation; 71: preservation; 72: invalidation proceeding; 73: oral hearing; 74: defense declassification; 75: dual filing; 76: term extension. |
| `SIMPLE_LEGAL_STATUS` | Simple legal status | Number | SIMPLE_LEGAL_STATUS:1 0: inactive; 1: active; 2: pending; 220: PCT designation period ended; 221: PCT designation period open; 999: unconfirmed. |
| `EFAM_STATUS` | Patsnap family status | Number | EFAM_STATUS:1 0: inactive; 1: active; 2: pending; 999: unconfirmed. |
| `UP_STATUS` | Unified Patent Court status | Number | UP_STATUS:1 0: not opted out; 1: opted out; 2: opt-out withdrawn; 3: unitary patent registered. |
| `ENTRY_COUNTRY_LS` | National entry legal status | Number | ENTRY_COUNTRY_LS:3 1: published; 2: substantive examination; 3: granted; 8: prevention of double patenting; 11: withdrawn; 12: withdrawal, unspecified; 17: deemed withdrawn; 18: voluntarily withdrawn; 13: rejected; 14: fully revoked; 15: term expired; 16: unpaid renewal fee; 21: rights restored; 22: rights terminated; 23: partially invalidated; 24: application terminated; 30: abandoned; 19: deemed abandoned; 20: voluntarily abandoned; 25: abandonment, unspecified. |
| `ENTRY_COUNTRY_SLS` | National entry simple legal status | Number | ENTRY_COUNTRY_SLS:1 0: inactive; 1: active; 2: pending; 999: unconfirmed. |
| `EPDS_LS` | EP designated country/region legal status | Number | EPDS_LS:3 3: granted; 14: fully revoked; 15: term expired; 16: unpaid renewal fee; 21: rights restored; 22: rights terminated; 23: partially invalidated; 30: abandoned; 19: deemed abandoned; 20: voluntarily abandoned; 25: abandonment, unspecified. EPDS_LS:"3" includes EP patents granted in a designated state and granted national patents entering through EP. Deemed abandonment includes failure to complete validation through timely translation/fee submission; voluntary abandonment is an express filing by the applicant. Granted includes effective national rights and automatic effect under the London Agreement pending national confirmation. |
| `EPDS_SLS` | EP designated country/region simple legal status | Number | EPDS_SLS:1 0: inactive; 1: active; 999: unconfirmed. Active includes completed national validation or automatic effect under the London Agreement pending confirmation. Inactive includes failure to take effect or subsequent lapse from expiry, abandonment/withdrawal, unpaid renewal fees or full invalidation. Unconfirmed includes non-London Agreement states where requirements may be met but timely fee/translation completion is not confirmed; the specific rights position remains unresolved. |
| `PV` | Patent value | Number | PV:[10000 TO 50000] PV:10000 |
| `PAGE_COUNT` | Document page count | Number | PAGE_COUNT:[5 TO 10] PAGE_COUNT:5 Available for selected countries/regions only.。Page count is the patent PDF page count. Design patents are excluded. |
| `CLAIM_COUNT` | Claim count | Number | CLAIM_COUNT:[10 TO 20] CLAIM_COUNT:10 |
| `FCLMS_WORDCOUNT` | First claim length | Number | FCLMS_WORDCOUNT:[100 TO 300] Chinese and English originals only: Chinese characters or English words are counted. |
| `AN_COUNT` | Original applicant/assignee count | Number | AN_COUNT:[2 TO 3] AN_COUNT:2 |
| `ANC_COUNT` | Current applicant/assignee count | Number | ANC_COUNT:[2 TO 3] ANC_COUNT:2 |
| `IN_COUNT` | Inventor count | Number | IN_COUNT:[2 TO 3] IN_COUNT:2 |
| `CPC_COUNT` | CPC classification count | Number | CPC_COUNT:[2 TO 3] CPC_COUNT:2 |
| `IPC_COUNT` | IPC classification count | Number | IPC_COUNT:[2 TO 3] IPC_COUNT:2 |
| `GOV` | Government interest | Text | GOV:1 Supports US patents only. |
| `EXAMINE_PERIOD` | Examination duration | Number | EXAMINE_PERIOD:[5 TO 10] EXAMINE_PERIOD:5 Months between substantive examination becoming effective and grant publication for invention patents. Available for selected countries/regions only. |
| `PATENT_TYPE` | Patent type | Text | PATENT_TYPE:D A: invention application; B: granted invention; U: utility model; D: design. |
| `PCTENTRY_TYPE` | Patents entering via the PCT route | Text | PCTENTRY_TYPE:1 Includes WO patents with national-entry data and national patents entering via the PCT route. |
| `EP_ENTRY` | Patents entering via the EPO route | Text | EP_ENTRY:1 Includes granted EP patents with entry-country data and national patents entering via the EP route. |
| `ENTRY_COUNTRY` | Entry country/region | Text | ENTRY_COUNTRY:DE Searches patents that entered a specified country/region. Includes EP validations, PCT national phase entries and direct national applications. |
| `SEP` | All standard-essential patents | Number | SEP:1 |
| `SEP_NUMBER` | Standard number | Text | SEP_NUMBER:"TS 138 211" Complete standard numbers only. |
| `SEP_TITLE` | SEP standard title | Text | SEP_TITLE:E-UTRA English search only. |
| `SEP_SOURCE` | SEP data source | Text | SEP_SOURCE:ETSI Sources: ETSI/IEC/IEEE/ISO/ANSI/CEN/ITU |
| `SEP_PROJECT` | Standard project | Text | SEP_PROJECT:5G English search only. |
| `SEP_DECLARANT` | SEP declarant | Text | SEP_DECLARANT:huawei English search only. |
| `AWARD_NAME` | Award name | Text | AWARD_NAME:(中国专利奖) Supports CN and European patents only. |
| `AWARD_LEVEL` | Award level | Text | AWARD_LEVEL:(金奖) CN patents only; use the complete award level, e.g. first/second/third prize, excellence, silver, gold, grand prize, design excellence/design gold/design silver. |
| `AWARD_SESSION` | Award session | Text | AWARD_SESSION:(第一届) Supports CN and European patents only. |
| `SUB_CASE` | Divisional applications | Identifier | SUB_CASE:(US10/771529) Retrieves all divisional applications using the parent application number. |
| `PRIORITY_COUNTRY_COUNT` | Priority country/region count | Number | PRIORITY_COUNTRY_COUNT:[10 TO 20] PRIORITY_COUNTRY_COUNT:10 |
| `PRIORITY_EMPTY` | Patents without priority | Number | PRIORITY_EMPTY:1 0: has priority; 1: no priority. |

## Litigation

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `LITIGATION` | Patent litigation | Number | LITIGATION:1 Available for selected countries/regions only. |
| `CASENO` | Case number | Text | CASENO:("(2012)浙杭知初字第425号") Available for selected countries/regions only. |
| `COURT` | Trial court | Text | COURT:(浙江省杭州市中级人民法院) Available for selected countries/regions only. |
| `JUDGE` | Judge | Text | JUDGE:(王江桥) Available for selected countries/regions only. |
| `CHIEF_JUDGE` | Presiding judge | Text | CHIEF_JUDGE:张艳培 Available for selected countries/regions only. |
| `PLAINTIFF` | Plaintiff | Text | PLAINTIFF:(华为) Available for selected countries/regions only. |
| `DEFENDANT` | Defendant | Text | DEFENDANT:(中兴) Available for selected countries/regions only. |
| `FILING_DATE` | Case filing date | Date | FILING_DATE:[20150101 TO 20150630] Available for selected countries/regions only. |
| `VERDICT_DATE` | Judgment date | Date | VERDICT_DATE:[20150101 TO 20151231] Available for selected countries/regions only. |
| `HEARING_DATE` | Hearing date | Date | HEARING_DATE:[20150101 TO 20151231] Available for selected countries/regions only. |
| `TRIAL_GRADE` | Proceeding stage | Text | TRIAL_GRADE:(一审) Available for selected countries/regions only. |
| `CASE_NATURE` | Case nature | Text | CASE_NATURE:(民事案件) Available for selected countries/regions only. |
| `CASE_LEVEL` | Case category | Text | CASE_LEVEL:(1) Supports CN patents only. 1: typical case; 2: ordinary case. |
| `CASE_REGION` | Trial region | Text | CASE_REGION:(江苏) Available for selected countries/regions only. |
| `CASE_TITLE` | Case title | Text | CASE_TITLE:(华为) Available for selected countries/regions only. |
| `CASE_FULL_TEXT` | Case full text | Text | CASE_FULL_TEXT:(照明) Available for selected countries/regions only. |
| `LIT_CLOSEDT` | Case closure date | Date | LIT_CLOSEDT:[20150101 TO 20151231] Available for selected countries/regions only. |
| `OUTCOME_JUDGEMENT` | Prevailing party | Text | OUTCOME_JUDGEMENT:(原告) |
| `OUTCOME_STATUS` | Case status | Text | OUTCOME_STATUS:("Closed (closed)") Available for selected countries/regions only. |
| `LITIGATION_COUNT` | Litigation count | Number | LITIGATION_COUNT:2 Available for selected countries/regions only. |
| `CASE_DOC_TYPE` | Court document type | Text | CASE_DOC_TYPE:2 Supports CN patents only. 1: judgment; 2: ruling; 3: mediation; 4: decision; 5: other document. |
| `COURT_GRADE` | Court level | Text | COURT_GRADE:中级法院 Supports CN patents only. Examples: supreme, high, intermediate, basic and specialized courts. |
| `VERDICT` | Judgment outcome | Text | VERDICT:(驳回) US patent search is not currently supported. |
| `PARTY` | Party | Text | PARTY:(华为) Parties include plaintiffs, defendants and third parties. Available for selected countries/regions only. |
| `PARTY_AGENT` | Party representative | Text | PARTY_AGENT:(王佩佩) Representatives include those of plaintiffs, defendants and third parties. Available for selected countries/regions only. |
| `PARTY_LAWFIRM` | Party law firm | Text | PARTY_LAWFIRM:(广东非凡律师事务所) Available for selected countries/regions only. |
| `AMOUNT_PLAINTIFF` | Total damages sought | Number | AMOUNT_PLAINTIFF:[10000 TO 50000] Supports CN patents only. |
| `DAMAGES_AMOUNT` | Total damages awarded | Number | DAMAGES_AMOUNT:[10000 TO 50000] Supports CN patents only. |
| `FILING_YEAR` | Case filing year | Date | FILING_YEAR:[2011 TO 2012] Available for selected countries/regions only. |
| `LITIGATION_PRODUCT` | Product involved | Text | LITIGATION_PRODUCT:(真空运动瓶) Available for selected countries/regions only. |

## Licensing

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `LICENSE` | Patents with licensing records | Number | LICENSE:1 |
| `LICENSOR` | Licensor | Text | LICENSOR:(三星) Available for selected countries/regions only. |
| `LICENSEE` | Licensee | Text | LICENSEE:(小米) Available for selected countries/regions only. |
| `LICNO` | License registration number | Text | LICNO:2014510000101 Available for selected countries/regions only. |
| `EXCLUSIVITY` | License exclusivity | Text | EXCLUSIVITY:(Exclusive) Available for selected countries/regions only. |
| `LIC_EFDT` | License effective date | Date | LIC_EFDT:[20160101 TO 20160501] Available for selected countries/regions only. |
| `LICENSE_COUNT` | License count | Number | LICENSE_COUNT:2 |

## Transfers

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `TRANSFER` | Patents with transfer records | Number | TRANSFER:1 |
| `TRANSFER_BEFORE` | Assignor | Text | TRANSFER_BEFORE:(英特尔) Available for selected countries/regions only. |
| `TRANSFER_AFTER` | Assignee | Text | TRANSFER_AFTER:(华为) Available for selected countries/regions only. |
| `TRANS_EFDT` | Transfer effective date | Date | TRANS_EFDT:[20180701 TO 20181231] Available for selected countries/regions only. |

## Reexamination and invalidation

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `REEXAMINVALID` | Patents with reexamination/invalidation records | Number | REEXAMINVALID:1 Available for selected countries/regions only. |
| `RI_APPLICANT` | Reexamination/invalidation petitioner | Text | RI_APPLICANT:彭宇轴 Available for selected countries/regions only. |
| `RIDN` | Decision number | Text | RIDN:(FS1112) Available for selected countries/regions only. |
| `RIIN` | Internal case number | Text | RIIN:(F12964) Available for selected countries/regions only. |
| `RIDDT` | Decision/issuance date | Date | RIDDT:[20160101 TO 20160501] Available for selected countries/regions only. |
| `RIDTP` | Decision type | Text | RIDTP:(FS) Available for selected countries/regions only. |
| `RID` | Decision | Text | RID:(全部无效) Available for selected countries/regions only. |
| `RIDP` | Decision highlights | Text | RIDP:(技术方案) Available for selected countries/regions only. |
| `RIDSM` | Grounds | Text | RIDSM:(不符合专利法第22条第3款的规定) Available for selected countries/regions only. |
| `RILGS` | Legal basis | Text | RILGS:(专利法第22条第3款) Available for selected countries/regions only. |
| `RI_FULL_TEXT` | Reexamination/invalidation full text | Text | RI_FULL_TEXT:(技术问题) Supports CN patents only. |
| `INVALID_COUNT` | Invalidation count | Number | INVALID_COUNT:2 Available for selected countries/regions only. |

## Pledges

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `PLEDGE` | Patent pledge | Number | PLEDGE:1 |
| `PLEDGOR` | Pledgor | Text | PLEDGOR:auto Supports CN patent pledges and US security interests only. |
| `PLEDGEE` | Pledgee | Text | PLEDGEE:(SILICON VALLEY BANK) Supports CN patent pledges and US security interests only. |
| `PLEDGENO` | Pledge registration number | Text | PLEDGENO:2015990000410 Supports CN patent pledges and US security interests only. |
| `PLE_EFDT` | Pledge effective date | Date | PLE_EFDT:[20160101 TO 20160501] Supports CN patent pledges and US security interests only. |
| `PLE_STAGE` | Pledge filing stage | Text | PLE_STAGE:1 Supports CN patents only. |
| `PLEDGE_COUNT` | Pledge count | Number | PLEDGE_COUNT:2 |

## Workspaces

| Field code | Field name | Type | Examples and notes |
| --- | --- | --- | --- |
| `MWS` | My workspace | Text | MWS:\|WorkspaceA\FolderB\| Searches folders under My Workspace only; enclose the folder path in \|\|. |
| `CWS` | Corporate workspace | Text | CWS:\|WorkspaceA\FolderB\| Searches folders under Corporate Workspace only; enclose the folder path in \|\|. |
| `CCF_` | Corporate custom field | Text | CCF_PR:"标引值A" Enclose hierarchical/option field tag values in quotes. For URL fields, "not blank" means the field has a value. |
