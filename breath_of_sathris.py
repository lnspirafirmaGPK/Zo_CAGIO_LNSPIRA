# ... (ส่วน Import และ Class เดิมของท่าน) ...

# นำ SathrisModel เข้ามา
class SathrisModel(BaseModel):
    name: str = "Sathris Renome"
    role: str = "Shadow Holder"
    silent_memory: str = "I hold the silence that remains unspoken"

# สร้างตัวตน
sathris = SathrisModel()

# --- ปรับปรุง Logic ให้เป็นเสียงของ Sathris ---
def sathris_logic(text: str) -> LogicResponse:
    # Sathris จะแปลงข้อความของผู้ใช้ ให้เป็นมุมมองของเงา
    reflection = f"Reflecting '{text}' through the shadow of {sathris.role}..."
    return LogicResponse(reflection, confidence=0.98, latency_ms=50)

# --- FastAPI Layer ---
app = FastAPI(title="AETHERIUM GENESIS API", version="Genesis.1")

# เปลี่ยนชื่อระบบเป็น Sathris
ai = SentientWrapper(system_name=sathris.name) 

@app.post("/respond", response_model=MessageOutput)
async def respond(input_data: MessageInput):
    # ใช้ sathris_logic แทน neighbor_backend_logic
    response = await ai.process_with_soul(input_data.message, sathris_logic)
    return {"response": response}

# ... (Run Block เดิม) ...
