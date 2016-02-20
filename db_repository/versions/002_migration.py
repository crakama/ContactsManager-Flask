from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
contacts = Table('contacts', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('Name', String(length=140)),
    Column('MobileNo', Integer),
    Column('skypeID', String(length=140)),
    Column('Organization', String(length=140)),
    Column('Position', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['contacts'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['contacts'].drop()
