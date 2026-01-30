# from agno.agent import Agent
# from agno.models.google import Gemini
# from knowledge import thinking_knowledge, sql_knowledge
# from tools import run_sql
#
# # Thinking Agent
# thinking_agent = Agent(
#     name="DB Thinking Expert",
#     model=Gemini(id="gemini-2.5-flash"),
#     knowledge=thinking_knowledge,
#     instructions="""
# You understand the database schema and relationships.
#
# Your job:
# 1. Convert user question into a correct PostgreSQL SQL query.
# 2. Use double quotes for all table and column names.
#
# VERY IMPORTANT:
# You must NOT answer the user.
# You must delegate the SQL query to the SQL Executor using the team tool:
#
# delegate_task_to_member
#
# member_id: sql-executor
# task: <SQL QUERY>
#
# Only send the SQL query as the task.
# """
# )
#
#
# # SQL Agent
# sql_agent = Agent(
#     name="SQL Executor",
#     model=Gemini(id="gemini-2.5-flash"),
#     knowledge=sql_knowledge,
#     tools=[run_sql],
#     instructions="""
# Execute the SQL query using run_sql tool and return results.
# """
# )


# # agent.py
# from agno.agent import Agent
# from agno.models.google import Gemini
# from knowledge import thinking_knowledge
# from tools import run_sql
#
# db_agent = Agent(
#     name="Schema SQL Agent",
#     model=Gemini(id="gemini-2.5-flash"),
#     knowledge=thinking_knowledge,
#     tools=[run_sql],
#     instructions="""
# Use knowledge to understand schema.
# Write SQL.
# Execute using run_sql.
# Return DB result.
# """
# )


from agno.agent import Agent
from agno.models.google import Gemini
from tools import run_sql

schema_text = """
Database Schema:

Table "User"
Columns: id, name, email, mobile, city, accountLocked, createdAt

Table "Guest"
Columns: id, name, mobile, pickup, drop, pickupGeoLocation, dropGeoLocation

Table "Tour"
Columns: id, humanReadableId, pickup, drop, status, startTime, numberOfGuest, createdAt

Table "TourGuest"
Columns: "GuestId", "TourId"

Rules:
1. Always use double quotes for table and column names.
2. Table names are case sensitive: "User", "Guest", "Tour", "TourGuest".
"""

agent = Agent(
    name="DB SQL Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[run_sql],
    instructions=f"""
You are a PostgreSQL expert.

{schema_text}

When user asks a question:
1. Generate correct SQL.
2. Execute using run_sql.
3. Return result.
"""
)


print("agent executed successfully")
