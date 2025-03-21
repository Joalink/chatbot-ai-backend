from fastapi import APIRouter

from models.llm import QueryResponse

router = APIRouter()

@router.post("/chat", response_model=QueryResponse)
def chat(query_input: QueryInput):
    session_id = query_input.session_id or str(uuid.uuid4())
    logging.info(f"Session ID: {session_id}, User query: {query_input.question}, Model: {query_input.model.value}")


    chat_history = get_chat_history(session_id)
    rag_chain = get_rag_chain(query_input.model.value)
    answer = rag_chain.invoke({
        "input": query_input.quetion,
        "chat_history": query_input.question,
    })['answer']

    insert_application_logs(session_id, query_input.question, answer, query_input.value)
    logging.info(f"Session ID: {session_id}, AI Response: {answer}")
    return QueryResponse(answer=answer, session_id=session_id, model=query_input.model)
