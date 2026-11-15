# Jenkins Demo: Calculator

Простой Python-калькулятор с pytest-тестами для демонстрации Jenkins Pipeline.

## Локальный запуск

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

## Jenkins

1. Создай Pipeline job в Jenkins.
2. Укажи этот репозиторий / путь к `Jenkinsfile`.
3. На агенте должны быть `python3` и `pip`.
4. Запусти Build — stages: **Setup** → **Test**.

Результаты тестов появятся во вкладке **Test Result** (JUnit XML).
