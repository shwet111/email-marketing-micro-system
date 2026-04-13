# Email Marketing Micro-System (POC)

## Overview

This project demonstrates a basic high-volume email sending system with asynchronous processing, personalization, and delivery tracking.

## Features

* Upload CSV to send bulk emails
* Personalized email generation (Jinja2)
* Asynchronous processing using FastAPI BackgroundTasks
* Domain rotation strategy
* Bounce handling endpoint
* Email status tracking using SQLite

## Architecture

The system follows a decoupled pipeline:
Upload → Processing → Personalization → Sending → Tracking

## Tech Stack

* Python (FastAPI)
* Jinja2
* SQLite

## How to Run

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000

## API Endpoints

* POST /upload → Upload CSV file
* POST /bounce → Handle bounce updates

## Notes

* Email sending is simulated for demonstration purposes
* Designed to be easily extendable with real queue systems (Celery + Redis)



## Architecture Diagram

                                            ┌───────────────┐
                                            │     UI        │
                                            │ Upload CSV    │
                                            └──────┬────────┘
                                                │
                                                ▼
                                            ┌───────────────┐
                                            │   FastAPI     │
                                            │  (API Layer)  │
                                            └──────┬────────┘
                                                │
                                                ▼
                                    ┌──────────────────────────┐
                                    │ Background Task Queue    │
                                    │ (Async Processing)       │
                                    └──────────┬───────────────┘
                                                │
                                                ▼
                                    ┌──────────────────────────┐
                                    │ Email Worker             │
                                    │ - Personalization        │
                                    │ - Domain Rotation        │
                                    │ - Send Email (Simulated) │
                                    └──────────┬───────────────┘
                                                │
                                                ▼
                                        ┌───────────────┐
                                        │ SQLite DB     │
                                        │ Status Track  │
                                        └───────────────┘
                                                │
                                                ▼
                                    ┌────────────────────┐
                                    │ Bounce API         │
                                    │ Updates Status     │
                                    └────────────────────┘


## Author

Shwet Garg
