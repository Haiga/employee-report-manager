# employee-report-manager

Basic Django app for employee and report management for Ssys test


# Run on docker

> docker-compose build

> docker-compose up -d

> docker exec -it employee-report-manager_web_1 /usr/local/bin/python manage.py migrate

> docker exec -it employee-report-manager_web_1 /usr/local/bin/python manage.py createsuperuser

Basic endpoints:

## API with employees CRUD:
### GET: /employees/ (employee list)
### POST: /employees/ (employee create)
### UPDATE /employees/ID/ (employee update)
### DELETE /employees/ID/ (employee delete)
### GET /employees/ID/ (employee detail)

## API with reports:
### GET /reports/employees/salary/ (salary report)
### GET /reports/employees/age/ (age report)

