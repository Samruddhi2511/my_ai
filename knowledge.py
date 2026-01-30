

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
