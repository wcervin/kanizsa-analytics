#!/usr/bin/env python3
"""
Kanizsa Analytics Service API
Provides data processing and analytics capabilities
"""

import os
import time
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'service': 'kanizsa-analytics'
    })

@app.route('/spark/status')
def spark_status():
    """Check Spark cluster status"""
    try:
        response = requests.get('http://spark-master:8080', timeout=5)
        return jsonify({
            'status': 'connected',
            'spark_master': 'http://spark-master:8080'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        })

@app.route('/flink/status')
def flink_status():
    """Check Flink cluster status"""
    try:
        response = requests.get('http://flink-jobmanager:8081', timeout=5)
        return jsonify({
            'status': 'connected',
            'flink_jobmanager': 'http://flink-jobmanager:8081'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        })

@app.route('/clickhouse/status')
def clickhouse_status():
    """Check ClickHouse status"""
    try:
        response = requests.get('http://clickhouse:8123/ping', timeout=5)
        return jsonify({
            'status': 'connected',
            'clickhouse': 'http://clickhouse:8123'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        })

@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'service': 'Kanizsa Analytics Service',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'spark_status': '/spark/status',
            'flink_status': '/flink/status',
            'clickhouse_status': '/clickhouse/status'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
