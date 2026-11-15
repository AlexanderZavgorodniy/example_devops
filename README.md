# Jenkins Demo: Calculator

Простой Python-калькулятор с pytest и coverage для демонстрации Jenkins Pipeline.

## Локальный запуск

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

HTML-отчёт покрытия: `htmlcov/index.html`

Документация API: [docs/calculator.md](docs/calculator.md)

## Jenkins

Pipeline stages: **Setup** → **Test**.

Артефакт: `htmlcov/` — HTML-отчёт покрытия.

Репозиторий: `https://github.com/AlexanderZavgorodniy/example_devops`
