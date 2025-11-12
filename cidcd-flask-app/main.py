"""Entry point for running the Flask app with configurable port."""

import os
from app import app

def main():
    """Run the Flask app on the specified host and port."""
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()