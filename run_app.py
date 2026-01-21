#!/usr/bin/env python
"""
Run the Ayurveda website Flask app
"""
import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from app import app
    
    logger.info("Flask app imported successfully")
    
    # Run the app
    logger.info("Starting Ayurveda website server...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )
    
except Exception as e:
    logger.error(f"Error starting app: {e}", exc_info=True)
    sys.exit(1)
