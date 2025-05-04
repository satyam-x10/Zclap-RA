Here’s the **updated and complete instruction** to run your project using Docker or manually (for both frontend and backend):

---

## 🚀 Running the Project

### 🐳 Option 1: Run with Docker

1. **Ensure Docker Desktop is running** on your system.
2. Open a terminal in the root directory of the project.
3. Run the following command:

```bash
docker-compose up --build
```

This will:

* Build and run the **frontend** (served with Nginx).
* Build and run the **backend** (FastAPI with OpenCV support).

### 🔗 Access the app:

* Frontend: [http://localhost:5173](http://localhost:5173) *(served via Nginx)*
* Backend API: [http://localhost:8000](http://localhost:8000)


---

### 🛠️ Option 2: Run Manually (if Docker doesn't work)

#### ▶️ Frontend (Vite)

```bash
cd frontend
yarn install
yarn run dev
```

* Open [http://localhost:5173](http://localhost:5173)

#### ▶️ Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* Open [http://localhost:8000](http://localhost:8000)

---


These configuration should work fine for windows