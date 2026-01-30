# # knowledge.py
# from agno.knowledge import Knowledge
#
# #  Knowledge for Thinking Agent (schema + relations)
# thinking_schema = """
# You are aware of full PostgreSQL schema and relations.
#
# TABLE "Guest"
# - id (uuid, primary key)
# - name
# - mobile
# - pickup
# - drop
#
# TABLE "Tour"
# - id (uuid, primary key)
# - pickup
# - drop
# - status
# - numberOfGuest
# - "DriverId"
# - "VehicleId"
#
# TABLE "TourGuest"
# - "GuestId" -> "Guest".id
# - "TourId"  -> "Tour".id
#
# TABLE "Driver"
# - "UserId" -> "User".id
#
# TABLE "User"
# - id
# - name
# - city
#
# All table and column names are case sensitive and must be in double quotes.
# """
#
# thinking_knowledge = Knowledge([thinking_schema])
#
#
# # Knowledge for SQL Agent (only execution rules, no thinking)
# sql_rules = """
# You do NOT think about schema.
#
# You only execute SQL queries provided to you using the run_sql tool.
#
# Return results exactly as received from DB.
# """
#
# sql_knowledge = Knowledge([sql_rules])


# from agno.knowledge import Knowledge
# from agno.knowledge.vectordb.chromadb import ChromaDB
# from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
#
# embedder = SentenceTransformerEmbedder(model="all-MiniLM-L6-v2")
#
# vectordb = ChromaDB(
#     collection_name="db_schema",
#     persist_directory="./chroma_db",
#     embedder=embedder,
# )
#
# schema_text = """
# TABLE "Guest"(id, name, mobile, pickup, drop)
# TABLE "Tour"(id, pickup, drop, status, "DriverId", "VehicleId")
# TABLE "TourGuest"("GuestId", "TourId")
# TABLE "User"(id, name, city)
# """
#
# thinking_knowledge = knowledge(
#     texts=[schema_text],
#     vectordb=vectordb,
# )
#
# from agno.agent import Agent
# from agno.knowledge.knowledge import Knowledge
# from agno.vectordb.chroma import ChromaDb
#
# # Create Chroma vector DB
# vector_db = ChromaDb(
#     collection="db_schema",
#     path="tmp/chromadb"
# )
#
# knowledge = Knowledge(vector_db=vector_db)
#
# # Insert your schema as knowledge
# schema_text = """
# TABLE "Guest"(id, name, mobile, pickup, drop)
#
# TABLE "Tour"(id, pickup, drop, status)
#
# TABLE "TourGuest"("GuestId", "TourId")
#
# TABLE "User"(id, name, city)
#
# Relations:
# Guest.id = TourGuest."GuestId"
# Tour.id = TourGuest."TourId"
# """

print("knowledge is running")

# knowledge.py

from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb

vectordb = ChromaDb(
    collection="db-schema",
    path="tmp/chromadb"
)

#knowledge object
knowledge = Knowledge(
    vector_db=vectordb
)

# DB Schema
schema_text = """
TABLE "Guest" (
    id,
    name,
    mobile,
    pickup,
    drop
)

TABLE "Tour" (
    id,
    pickup,
    drop,
    status
)

TABLE "TourGuest" (
    "GuestId",
    "TourId"
)

TABLE "User" (
    id,
    name,
    city
)
"""

# ---------- Insert into Knowledge
# Agno will chunk, embed, and store automatically
knowledge.insert(schema_text)



print("knowledge is done")


# knowledge.py

from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb

# Create vector DB for knowledge
vector_db = ChromaDb(
    collection="db_schema",
    path="tmp/chromadb"
)

knowledge = Knowledge(vector_db=vector_db)

# ---------- ACTUAL DATABASE SCHEMA FROM YOUR SCREENSHOTS ----------

schema_text = """
DATABASE TABLES AND RELATIONSHIPS

TABLE "User"
COLUMNS:
id, password, email, name, mobile, whatsAppNo,
street1, street2, PIN, city, state,
isSystemGeneratedPassword, accountExpire, accountLocked,
passwordExpired, lastLoginAt, profilePic,
createdAt, updatedAt, revision, createdBy, updatedBy

IMPORTANT:
- City information exists ONLY in this table in column "city".

------------------------------------------------------------

TABLE "Guest"
COLUMNS:
id, name, mobile, alternateMobile, isPrimary,
profilePic, pickupGeoLocation, dropGeoLocation,
pickTime, sequence, pickup, drop,
revision, createdBy, updatedBy

IMPORTANT:
- Guest DOES NOT have city.
- Guest is linked to User using:
    Guest.createdBy -> User.id

------------------------------------------------------------

TABLE "Tour"
COLUMNS:
id, humanReadableId, pickup, drop,
pickupGeoLocation, dropGeoLocation,
status, bookingRequest, numberOfGuest,
paymentMethod, note, vehicalType,
startTime, garaTime, endTime,
startDate, endDate, createdBy,
enablePinVerification, isMultiLocation,
withAc, contactPerson, createdAt,
updatedAt, ClientId, DriverId,
PackageId, VehicleId, VendorId,
OrganizationId, pickupTime, revision,
isForEmployee, updatedBy, tourInfo,
remark, isDriverCreated

------------------------------------------------------------

TABLE "TourGuest"
COLUMNS:
GuestId, TourId, revision, costCenterId

RELATIONSHIPS:
TourGuest.GuestId  -> Guest.id
TourGuest.TourId   -> Tour.id

------------------------------------------------------------

QUERY RULES FOR AGENT:

1. If question asks about city → use "User"."city"
2. If question asks Guests from a city:
      JOIN Guest.createdBy = User.id
3. If question asks Guest tour details:
      JOIN Guest -> TourGuest -> Tour
4. Always use DOUBLE QUOTES for table and column names.
"""

# Insert schema into knowledge base
knowledge.insert(text_content=schema_text)

print("✅ Knowledge loaded with real DB schema")
