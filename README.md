If the app stucks, I checked all uvicorn instances running by the following command

tasklist /FI "IMAGENAME eq python.exe"

And terminated them with the following commands. PID can be found from the previous list

taskkill /PID <PID_ID_REPLACE_HERE>  /F

Para inicia la applicacion:
uvicorn app.main:app --reload 

alembic manual migrations 