# AICTEFlow — SIH approval workflow demonstration

This is a local educational prototype for the SIH project **Integrated AICTE Approval Workflow Automation, Compliance Monitoring and Alert Management System**. The existing React dashboard and styling are retained, with a Flask/SQLite backend and connected workflow screens.

**Important:** This is not an official AICTE service and is not production-ready. Document screening produces advisory risk flags; it cannot prove forgery or authenticity. Application document requirements and regulatory thresholds are configurable demo placeholders and must be checked against authoritative rules before real use. No official AICTE integration is included.

### Review-deadline ownership

Institution users do not select or edit the review deadline. Drafts have no deadline. After required-document and integrity checks pass on submission, the backend assigns a configurable local-demo target (`DEMO_REVIEW_SLA_DAYS`, default 30 days). Authorized AICTE officers can revise it from application edits, with a mandatory reason and audit log. This demo default is illustrative and is not an official AICTE SLA.

## Included workflow areas

- Institution registration/login; officer, EVC committee, and authority demo roles created by an administrator through the account script.
- Draft creation, required-document progression, server uploads, final submission checks, stage changes with reasons, officer assignment, decisions, case history, standard in-app communications, and case summaries.
- PDF/PNG/JPG/JPEG file signature checks, SHA-256 exact-duplicate screening, near-duplicate extracted-text comparison, dummy/alteration/signature wording flags, basic document-type mismatch checks, unreadable-document flags, and officer manual review with access to the original and possible match.
- EVC scheduling/completion, undertaking/compliance records and evidence, document expiry and renewal verification, persistent deadline/deficiency/expiry/EVC/compliance alerts, configurable demo thresholds, and consolidated database-backed reports.
- Optional SMTP digest delivery and a script suitable for Windows Task Scheduler. Email remains disabled until SMTP and the demo rule are configured.

The project includes a starter SQLite database and sample uploads from the supplied demo. The app adds missing tables and performs limited additive SQLite migrations on startup. Back up the database before replacing a project version. Never include real student, institution or confidential data in a demo archive.

## Requirements

- Windows 10/11 and PowerShell
- Python 3.12 recommended (Python 3.11 may also work; check dependencies before using another version)
- Node.js 22 LTS or a compatible current LTS release with npm
- Optional scanned-document OCR: Tesseract OCR installed separately and its executable added to `PATH`

## Setup — Terminal 1 (backend)

Extract the ZIP. Open PowerShell in the `AICTE_Approval` folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python seed_documents.py
```

If PowerShell blocks script activation, run this in the same terminal, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Create the accounts you will use. Each command prompts for an email and password; no default password is shipped:

```powershell
python create_user.py officer
python create_user.py committee
python create_user.py authority
```

You may create multiple accounts by running the command again with a different email. Institution accounts can register on the login screen. The `.env.example` is a template; the app loads `AICTE_Approval/.env`. If `SECRET_KEY` is blank, the app generates a local secret saved in `instance/.secret_key` (do not share that file). Leave `COOKIE_SECURE=0` for local HTTP development; set secure cookies only when using HTTPS.

Start the backend and keep this terminal open:

```powershell
python app.py
```

Backend health page: `http://localhost:5002/`

## Setup — Terminal 2 (frontend)

Open a second PowerShell window at the `sih-aicte` folder:

```powershell
npm ci
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173/`. Keep both terminals open. If Flask is on a different URL, create `sih-aicte/.env.local` containing:

```text
VITE_API_URL=http://localhost:5002
```

Restart Vite after changing `.env.local`.

## Demo workflow to test

1. Register an institution account; sign in.
2. Create an application draft, upload the required PDF/JPG/PNG documents in the configured order, then use **Submit for review**. Submission is refused until mandatory requirements have been uploaded.
3. Sign out. Sign in as the AICTE officer account created above.
4. Open **Document verification**. Review exact/near duplicate or other integrity flags, open the original file and the possible match, and record investigation, deficiency, or clearance with remarks.
5. For EVC, create an application assignment for the registered committee email, sign in as that committee account, and test schedule/completion actions. Use the authority account for decision-queue cases.
6. Open **EVC & compliance**, **Alerts & deadlines**, and **Reports** to exercise compliance evidence, document renewal, alert acknowledgement/closure, case communications/summaries, editable demo thresholds and CSV export.
7. Restart Flask and confirm that application/document/workflow records persist in SQLite.

## Tests

From `AICTE_Approval` with the virtual environment active:

```powershell
python -m compileall -q .
python -m unittest -v test_document_integrity.py test_backend.py
```

From `sih-aicte`:

```powershell
npm ci
npm run build
```

See `TEST_REPORT.md` for checks actually run in the preparation environment and limitations. Do not describe the project as fully validated until the backend tests and browser-level workflow tests pass on the target Windows machine.

## Scheduled alert emails (optional)

The app creates/refreshes persistent alerts when the alert centre loads. To refresh alerts on a schedule independent of user visits, use Windows Task Scheduler to run `AICTE_Approval/.venv/Scripts/python.exe AICTE_Approval/send_scheduled_alerts.py` with the working directory set to `AICTE_Approval`. Email is sent only if SMTP settings in `.env` are configured and `email_alerts_enabled` is set to `true` in the officer's **Configurable demonstration rules**. Configure only a mailbox you control. Do not put credentials in source code.

## Security and limitations

- Local demo only. No official system integration, production HTTPS deployment, independent security review, comprehensive CSRF/rate-limiting protection, or production threat testing is included.
- Role checks, session authentication, institution-owned application checks, and protected backend file routes are implemented but still require adversarial access tests.
- OCR depends on Tesseract being installed; scanned documents may not yield reliable text.
- Text similarity, hashes, placeholder markers and missing-signature wording are risk signals, not proof of fraud. A qualified human must visually inspect the file and use trusted sources before a final decision.
- Email is optional and requires external SMTP setup. Regulatory rules and seeded document requirements are illustrative, not authoritative AICTE/APH rules.
- Only share sanitized demo data. Remove the included demo database/uploads if they are not appropriate for your submission.
