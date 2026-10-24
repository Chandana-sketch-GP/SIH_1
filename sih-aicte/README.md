# AICTEFlow — SIH Frontend Prototype

A responsive React + Vite frontend for an AICTE approval workflow with two role-based portal experiences:

- **Institution portal:** submit an application, attach documents, view application status and add documents to a submission.
- **AICTE Officer portal:** review applications, assign officers, change workflow stage, approve/reject/request corrections, review document status, monitor deadlines and export CSV reports.

## Start the project

Requirements: Node.js 18+ (Node 20 LTS recommended) and npm.

```bash
npm install
npm run dev
```

Open the local URL printed by Vite (normally `http://localhost:5173`). For a production build:

```bash
npm run build
npm run preview
```

## Demo sign-in

Select either **Institution** or **AICTE Officer**, enter any valid-looking email and any password, and sign in. This is intentionally a demo sign-in only; it does not validate credentials or provide secure role authorization.

- Officer example: `officer@aicte.gov.in`
- Institution example: `office@college.edu.in`

The app persists application records and the demo session in browser `localStorage`. The initial sample records are provided to demonstrate officer workflows. A newly submitted institution application appears in the officer portal when you sign out and sign in as an officer in the **same browser**. The demo institution list is filtered by the contact email entered at sign-in; to see a newly created application as that institution, sign in using the same email entered in the application form.

## Important integration notes

This is a fully interactive frontend prototype, not a production approval service. Upload selection currently stores file names, sizes and verification metadata in localStorage; it does **not** persist file bytes or provide secure file preview/download. Browser localStorage is not a shared database between devices/browsers.

Before production or formal institutional use, connect the UI to your Flask backend and implement:

1. Server-side authentication and authorization for institution/officer roles.
2. A document table linked to `application_id`, plus secure upload/download routes and file-size/type validation.
3. Database-backed application, document, workflow and audit APIs; replace localStorage demo persistence with API calls.
4. Server-side validation, official AICTE deadlines/rules, notification delivery and audit trail.

The design palette follows the requested colors: navy `#0F172A`, saffron `#F97316`, peach `#FFEDD5`, canvas `#FAFAF9`, white `#FFFFFF`, approved green `#10B981`, deficient red `#EF4444`, and SLA rose `#E11D48`.
