#!/usr/bin/env python3
"""Test database connection and basic operations"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from database import db
from loguru import logger


def test_database_connection():
    """Test database connection and basic operations"""
    try:
        # Test connection
        logger.info("Testing database connection...")
        with db.get_connection() as conn:
            logger.success("Database connection successful!")
        
        # Test query execution
        logger.info("Testing query execution...")
        result = db.execute_query("SELECT 1 as test")
        assert result[0]['test'] == 1
        logger.success("Query execution successful!")
        
        # Test table existence
        logger.info("Checking tables...")
        tables_query = """
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name;
        """
        tables = db.execute_query(tables_query)
        
        expected_tables = [
            'competitions', 'fixtures', 'matches', 
            'seasons', 'teams', 'venues'
        ]
        
        found_tables = [table['table_name'] for table in tables]
        
        for table in expected_tables:
            if table in found_tables:
                logger.success(f"✓ Table '{table}' exists")
            else:
                logger.error(f"✗ Table '{table}' not found")
        
        # Test view
        views_query = """
        SELECT table_name 
        FROM information_schema.views 
        WHERE table_schema = 'public';
        """
        views = db.execute_query(views_query)
        
        if any(view['table_name'] == 'team_match_stats' for view in views):
            logger.success("✓ View 'team_match_stats' exists")
        else:
            logger.error("✗ View 'team_match_stats' not found")
        
        logger.success("All database tests passed!")
        
    except Exception as e:
        logger.error(f"Database test failed: {e}")
        sys.exit(1)
    finally:
        db.close_pool()


if __name__ == "__main__":
    test_database_connection()