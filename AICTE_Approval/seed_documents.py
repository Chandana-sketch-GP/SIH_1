
from app import app
from extensions import db
from models import DocumentRequirement

sample_documents = [
    {
        "document_name": "Application Form",
        "description": "Completed application form",
        "sequence_order": 1,
    },
    {
        "document_name": "Institution Registration Certificate",
        "description": "Registration details of the institution",
        "sequence_order": 2,
    },
    {
        "document_name": "Land or Lease Documents",
        "description": "Relevant land ownership or lease records",
        "sequence_order": 3,
    },
]

with app.app_context():
    for item in sample_documents:
        existing = DocumentRequirement.query.filter_by(
            application_type="New Institution",
            document_name=item["document_name"],
        ).first()

        if existing:
            print("Already exists:", item["document_name"])
            continue

        db.session.add(
            DocumentRequirement(
                application_type="New Institution",
                document_name=item["document_name"],
                description=item["description"],
                is_mandatory=True,
                sequence_order=item["sequence_order"],
            )
        )

    db.session.commit()
    print("Sample document requirements added.")
