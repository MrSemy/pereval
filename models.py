import datetime

from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, VARCHAR, BigInteger, LargeBinary, TIME, TIMESTAMP


metadata = MetaData()

pereval_added = Table(
    'pereval_added',
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('beauty_title', String),
    Column('title', String),
    Column('other_titles', String),
    Column('connect', String),
    Column('add_time', TIME),
    Column('date_added', TIMESTAMP(timezone=False), default=datetime.datetime.now()),
    Column('status', String, nullable=False, server_default='new'),
    Column('level_winter', String),
    Column('level_summer', String),
    Column('level_autumn', String),
    Column('level_spring', String),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('coord_id', Integer, ForeignKey('coords.id'))
)

pereval_images = Table(
    'pereval_images',
    metadata,
    Column('pereval_id', Integer, ForeignKey('pereval_added.id')),
    Column('image_id', Integer, ForeignKey('images.id'))
)

coords = Table(
    'coords',
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('latitude', VARCHAR),
    Column('longitude', VARCHAR),
    Column('height', Integer)
)

users = Table(
    'users',
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('fam', String),
    Column('name', String),
    Column('otc', String),
    Column('email', String, nullable=False, unique=True),
    Column('phone', String)
)

images = Table(
    'images',
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('img', LargeBinary),
    Column('date_added', TIMESTAMP(timezone=False), default=datetime.datetime.now()),
    Column('title', String)
)

perval_areas = Table(
    'perval_areas',
    metadata,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('id_parent', Integer, nullable=False),
    Column('title', String)
)

spr_activities_types = Table(
    'spr_activities_types',
    metadata,
    Column('id', BigInteger, primary_key=True, nullable=False),
    Column('title', String)
)