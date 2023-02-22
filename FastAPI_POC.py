#!/usr/bin/env python3
# coding: utf-8

import sys

import uvicorn
from fastapi import FastAPI


class FastAPI_POC:
    host = "127.0.0.1"
    port = "8888"
    api = FastAPI(title="FastAPI POC", version="Alpha")
    
    def __init__(self):
        if len(sys.argv) == 1:
            host = self.host
            port = int(self.port)
        elif len(sys.argv) == 2:
            host = sys.argv[1]
            port = int(self.port)
        elif len(sys.argv) == 3:
            host = sys.argv[1]
            port = int(sys.argv[2])
        uvicorn.run("FastAPI_POC:FastAPI_POC.api", host=host, port=port, reload=True)
    
    @api.get("/", description="This is the root")
    def root():
        return f"{FastAPI_POC.api.title} - {FastAPI_POC.api.version}"

if __name__ == "__main__":
    FastAPI_POC()
