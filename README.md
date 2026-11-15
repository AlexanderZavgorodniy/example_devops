# Jenkins Demo: Calculator

Простой Python-калькулятор с pytest, coverage и документацией для демонстрации Jenkins Pipeline.

## Локальный запуск

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

После тестов:

- покрытие в терминале
- HTML-отчёт: `htmlcov/index.html`
- XML: `coverage.xml`

Документация API: [docs/calculator.md](docs/calculator.md)

## Jenkins

Pipeline stages: **Setup** → **Test** → **Docs**.

Артефакты сборки:

- `test-reports/results.xml` — результаты pytest
- `coverage.xml` + `htmlcov/` — отчёт покрытия
- `docs/` — документация

Репозиторий: `https://github.com/AlexanderZavgorodniy/example_devops`
