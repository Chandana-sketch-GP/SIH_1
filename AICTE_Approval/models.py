

from extensions import db
from datetime import datetime


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    institution_name = db.Column(db.String(200), nullable=False)
    application_type = db.Column(db.String(100), nullable=False)

    current_stage = db.Column(db.String(100), default="Submitted")
    status = db.Column(db.String(50), default="Pending")

    submission_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    deadline = db.Column(db.DateTime, nullable=True)
    assigned_officer = db.Column(db.String(150), nullable=True)
    remarks = db.Column(db.Text, nullable=True)


class WorkflowStage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("application.id"),
        nullable=False
    )

    stage_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    assigned_to = db.Column(db.String(150), nullable=True)
    started_at = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    remarks = db.Column(db.Text, nullable=True)


class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("application.id"),
        nullable=False
    )

    action = db.Column(db.String(200), nullable=False)
    performed_by = db.Column(db.String(150), nullable=True)
    details = db.Column(db.Text, nullable=True)
    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


# Documents required for each application process
class DocumentRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    application_type = db.Column(db.String(100), nullable=False)
    document_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_mandatory = db.Column(db.Boolean, default=True)
    sequence_order = db.Column(db.Integer, nullable=False, default=1)


# Documents uploaded for an individual application
class UploadedDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("application.id"),
        nullable=False
    )

    requirement_id = db.Column(
        db.Integer,
        db.ForeignKey("document_requirement.id"),
        nullable=False
    )

    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    upload_status = db.Column(db.String(50), default="Uploaded")
    uploaded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    verified_by = db.Column(db.String(150), nullable=True)
    verified_at = db.Column(db.DateTime, nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    issue_date = db.Column(db.Date, nullable=True)
    expiry_date = db.Column(db.Date, nullable=True)
    proposed_issue_date = db.Column(db.Date, nullable=True)
    proposed_expiry_date = db.Column(db.Date, nullable=True)
    renewal_status = db.Column(
        db.String(50),
        nullable=False,
        default="Not Required"
    )
    renewed_document_id = db.Column(
        db.Integer,
        db.ForeignKey("uploaded_document.id"),
        nullable=True
    )

class EVCRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(
        db.Integer,
        db.ForeignKey("application.id"),
        nullable=False
    )
    committee_name = db.Column(db.String(200), nullable=True)
    scheduled_date = db.Column(db.DateTime, nullable=True)
    completed_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Pending")
    assigned_officer = db.Column(db.String(150), nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

class Undertaking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(
        db.Integer,
        db.ForeignKey("application.id"),
        nullable=False
    )
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")
    evidence_file = db.Column(db.String(500), nullable=True)
    submitted_at = db.Column(db.DateTime, nullable=True)
    verified_by = db.Column(db.String(150), nullable=True)
    verified_at = db.Column(db.DateTime, nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
