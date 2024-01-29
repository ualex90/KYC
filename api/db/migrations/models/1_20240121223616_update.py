from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "file" ALTER COLUMN "name" TYPE VARCHAR(100) USING "name"::VARCHAR(100);
        ALTER TABLE "file" ALTER COLUMN "content_type" TYPE VARCHAR(50) USING "content_type"::VARCHAR(50);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "file" ALTER COLUMN "name" TYPE VARCHAR(50) USING "name"::VARCHAR(50);
        ALTER TABLE "file" ALTER COLUMN "content_type" TYPE VARCHAR(30) USING "content_type"::VARCHAR(30);"""
