"""
Seed data for cybersecurity laws, guidelines, and government portals
This script populates the database with placeholder data that can be updated later
"""

from database import db


SEED_LAWS = [
    {
        'country_code': 'NYC',
        'title': 'New York SHIELD Act',
        'description': 'Placeholder: The New York SHIELD Act (Stop Hacks and Improve Electronic Data Security) is a comprehensive cybersecurity law. Additional details coming soon.',
        'category': 'Data Protection',
        'source_url': 'https://www.ny.gov'
    },
    {
        'country_code': 'NYC',
        'title': 'HIPAA (Health Insurance Portability and Accountability Act)',
        'description': 'Placeholder: Federal law that establishes privacy and security standards for healthcare data. Detailed information to be added.',
        'category': 'Healthcare Privacy',
        'source_url': 'https://www.hhs.gov'
    },
    {
        'country_code': 'GERMANY',
        'title': 'GDPR (General Data Protection Regulation)',
        'description': 'Placeholder: European Union regulation on data protection and privacy. More comprehensive details coming.',
        'category': 'Data Protection',
        'source_url': 'https://gdpr-info.eu'
    },
    {
        'country_code': 'GERMANY',
        'title': 'German IT Security Act (BSI)',
        'description': 'Placeholder: German law focusing on IT security and critical infrastructure protection. Additional research in progress.',
        'category': 'Cybersecurity',
        'source_url': 'https://www.bsi.bund.de'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'title': 'Personal Information Protection Act (PIPA)',
        'description': 'Placeholder: South Korean law protecting personal information. Detailed provisions to be added.',
        'category': 'Data Protection',
        'source_url': 'https://www.pipc.go.kr'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'title': 'Information and Communications Network Act',
        'description': 'Placeholder: Law regulating information and communications networks in South Korea. More details coming soon.',
        'category': 'Cybersecurity',
        'source_url': 'https://www.kisa.or.kr'
    }
]

SEED_GUIDELINES = [
    {
        'country_code': 'NYC',
        'name': 'NIST Cybersecurity Framework',
        'description': 'Placeholder: Guidelines for managing cybersecurity risk. Detailed framework information to be added.',
        'category': 'General Cybersecurity',
        'source_url': 'https://www.nist.gov'
    },
    {
        'country_code': 'NYC',
        'name': 'CIS Controls',
        'description': 'Placeholder: Best practices for cybersecurity controls. Additional details coming soon.',
        'category': 'Best Practices',
        'source_url': 'https://www.cisecurity.org'
    },
    {
        'country_code': 'GERMANY',
        'name': 'C5 Audit Catalog',
        'description': 'Placeholder: Cloud security audit standard in Germany. More information to be researched.',
        'category': 'Cloud Security',
        'source_url': 'https://www.bsi.bund.de'
    },
    {
        'country_code': 'GERMANY',
        'name': 'BSI C5 Baseline Protection',
        'description': 'Placeholder: BSI baseline security recommendations. Detailed guidelines coming soon.',
        'category': 'IT Security',
        'source_url': 'https://www.bsi.bund.de'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'name': 'KISA Security Guidelines',
        'description': 'Placeholder: Korean Internet & Security Agency cybersecurity guidelines. Additional details to be added.',
        'category': 'General Cybersecurity',
        'source_url': 'https://www.kisa.or.kr'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'name': 'Critical Infrastructure Protection Standards',
        'description': 'Placeholder: Standards for protecting critical infrastructure in South Korea. More research in progress.',
        'category': 'Infrastructure Security',
        'source_url': 'https://www.kisa.or.kr'
    }
]

SEED_PORTALS = [
    {
        'country_code': 'NYC',
        'portal_name': 'New York State Department of State',
        'url': 'https://www.ny.gov',
        'description': 'Placeholder: Official New York government portal for cybersecurity laws and regulations. Details to be updated.',
        'category': 'Government Portal'
    },
    {
        'country_code': 'NYC',
        'portal_name': 'Federal Trade Commission (FTC)',
        'url': 'https://www.ftc.gov',
        'description': 'Placeholder: Federal agency protecting consumers and businesses. More specific resources coming.',
        'category': 'Federal Agency'
    },
    {
        'country_code': 'GERMANY',
        'portal_name': 'Bundesamt fur Sicherheit in der Informationstechnik (BSI)',
        'url': 'https://www.bsi.bund.de',
        'description': 'Placeholder: German Federal Office for Information Security. Detailed information coming soon.',
        'category': 'Government Agency'
    },
    {
        'country_code': 'GERMANY',
        'portal_name': 'German Data Protection Authority (BfDI)',
        'url': 'https://www.bfdi.bund.de',
        'description': 'Placeholder: Federal Data Protection Commissioner office. Additional details to be added.',
        'category': 'Government Agency'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'portal_name': 'Korea Internet & Security Agency (KISA)',
        'url': 'https://www.kisa.or.kr',
        'description': 'Placeholder: South Korean cybersecurity authority. More comprehensive information coming.',
        'category': 'Government Agency'
    },
    {
        'country_code': 'SOUTH_KOREA',
        'portal_name': 'Personal Information Protection Commission (PIPC)',
        'url': 'https://www.pipc.go.kr',
        'description': 'Placeholder: South Korean personal information protection authority. Detailed resources to be added.',
        'category': 'Government Agency'
    }
]


def seed_database():
    """Populate database with seed data"""
    try:
        print("Checking if tables exist...")

        print("Seeding cybersecurity laws...")
        for law in SEED_LAWS:
            db.client.table('cybersecurity_laws').insert(law).execute()
        print(f"Added {len(SEED_LAWS)} laws")

        print("Seeding cybersecurity guidelines...")
        for guideline in SEED_GUIDELINES:
            db.client.table('cybersecurity_guidelines').insert(guideline).execute()
        print(f"Added {len(SEED_GUIDELINES)} guidelines")

        print("Seeding government portals...")
        for portal in SEED_PORTALS:
            db.client.table('government_portals').insert(portal).execute()
        print(f"Added {len(SEED_PORTALS)} portals")

        print("Database seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        print("Note: Tables may not exist yet. Run database migrations first.")


if __name__ == '__main__':
    seed_database()
