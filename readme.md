# Float Backend Candidate Assessment

Welcome to the Float Candidate Assessment for Backend developers.  We have details instructions on how to get started and what a successful solution will entail.  Please _read and follow_ the enclosed instructions.

## What are we building?

At the core of Float is our Django API which powers multiple front-facing client(s) - specifically the authentication, CRUD interfaces for models, permissions, and complex workflows.

In our sample application we are adding a webhook `/ehr_webhook/` to our API / Platform.  Your task is the implementation of the endpoint so that it returns a `201` even if duplicates exist, but returns `400x` and `500x` for invalid situations (for example malformed `json`) and ensure the tests are passing and there are no regressions.  You will do the work on a separate branch and submit a pull-request (_see below_ for Submit Solution).


### Expectations

- You can run a local compatible data-store for a [Django 4.x](https://www.djangoproject.com/) app
  - Alter `settings.py` as needed
- You can run a local python `env` with `pip`
- You can handle any build issues that can occur in a python environment
- You can run the projects test-suite
- Implement a version of the webhook in the 30-1hr time-allotment and be prepared to discuss/document the trade-offs (tech-debit, security, scale-ability)


### What We Provide

Setting up a new project is time intensive so we have done some of the upfront work.

- We provide you with a shell of a __Django__ app with working migrations, `requirements.txt` and working _tests_.
- Preconfigured data-store bindings for `sqlite` and `postgres`
- Sample webhook payloads the assignment/task.
- `API` Documentation
- Grading Solution Rubric (_see below_)

#### Our Rest API

We also are providing an initial endpoint for you to have as a basis

- __GET__ `/patient/` will return a list of patients
- __POST__ `/patient/` - As a __POST__ requires a json body with `email`, and `name` as required fields. Returns `201`

#### Assessment Details 

You are to implement a new webook endpoint that accepts the following `POST /ehr_webhook` that will contain an array of data as:

```json
[
  {"email":"pete@floatfi.com", "name": "Pete Townshend"},
  {"email":"Jane@floatfi.com", "name": "Jane Buckneer"}
]
```

To help you in your work here is an example of our vendors webhook all to our server

```shell
curl -X POST -H "Content-Type: application/json"  -d '[{"email":"pete@floatfi.com", "name": "Pete Townshend"},{"email":"Jane@floatfi.com", "name": "Jane Buckneer"}]' http://localhost:8000/ehr_webhook/
```
---

## QuickStart Guide

Here are a few first steps to get off the ground

```
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
```

At this point you should be able to do either of the following:

1. Run `python manage.py runserver`
2. Run `python manage.py test app`

---

## What is a Successful Solution

We want to ensure you submit a successful solution so here is our assessment grading rubric.

|  | Task / Skill-Check   | Description                                                                         |
|---|-------------------|-------------------------------------------------------------------------------------|
| :thumbsup: | Code Complete        | Did you complete the assessment in it's entirety in terms of functionality          |
| :white_check_mark: | CI Passes | We expect the __CI Runner__ using `github-actions` to pass. |
| :satellite: | API / Network Comms. | Were networking communications properly configured                                  |
| :thought_balloon: | Pull-Request         | Open up a proper PR, **_read the submission process below_**                            |
| :shipit: | Commit History       | We value [conventional-commits](https://www.conventionalcommits.org/en/v1.0.0)      |

---

## Submitting a Solution

### 1. Setting Up Your Solution

> __IMPORTANT:__ When you receive this zip file create your repository and __COMMIT__ the code as the `initial commit` inside of the _default branch_ `main` or `master`.

### 2. Create a Branch & PR

You should begin to build your solution on a new branch (_we don't care what you call it we recommend_ --  `solution`).  Once you are code complete, create a private repository and push up both branches.  And open up a pull-request against the _default branch_ `main|master`.

### 3. Finalize & Submit

Invite `mgan59`, `DanOB34`, `CMitchell08`, `ramirog89` to your repository so we can see your pull-request.  We also recommend assigning the PR to for review  so that we get notifications in our github-ui.

### 4. Review Process

Once the reviewers are added to the repository, we will conduct a quick PR review and setup a time to go over the code together.


