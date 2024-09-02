from flask import Blueprint, current_app, jsonify
from app.db.mysql_connector import fetch_last_10_records, fetch_last_50_records
from app.db import db_bp


@db_bp.route('/fetch_records', methods=['GET'])
def fetch_records():
    db_connection = current_app.config['DB_CONNECTION']
    records = fetch_last_10_records(db_connection)
    
    return jsonify(records), 200

@db_bp.route('/fetch_last_50_records', methods=['GET'])
def fetch_last_50_records_endpoint():
    db_connection = current_app.config['DB_CONNECTION']
    records = fetch_last_50_records(db_connection)
    
    return jsonify(records), 200