# 📄 Intel-Business-Contract-Validation
Business Contract Validation System
This project aims to develop a system to parse business contracts, classify clauses, and detect deviations from templates. The project includes both backend and frontend components.

# 🏗 Project Structur
Description: 
 Business contracts are legal documents. The first task is to parse these documents so that have a 
structure to them. Determine the key details within the contract document. Every contract has clauses 
and sub-clauses. The next step is to classify the contents of the parsed documents to these clauses. 
Typically, a contract has an associated template to it, and it is important to determine the deviations 
from that template and highlight them.

## Features
- Automated extraction and classification of contract clauses.
- Highlighting key entities such as dates, parties, and legal terms.
- Identifying deviations from standard contract templates.
- Providing a summarized view of the contract content.
  
# Project Structure
- backend/: Contains the backend code, including the Flask application and models.
- frontend/: Contains the frontend code, including React components and styles.

## 🛠 Requirements

- **Python 3.9**
- **Node.js 14**
- **Docker and Docker Compose**


### Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/business-contract-validation.git
   cd business-contract-validation
   ```
2. **Set up the Backend:**
   ```sh
cd backend
```
3. **Create a virtual environment and activate it:**
   - **Windows:**
     ```sh
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - **macOS/Linux:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Initialise the database**
   ```sh
   flask db init
flask db migrate
flask db upgrade
```
6. **Run the backend server**
   ```sh
python run.py
```
7. **Set up the frontend**
```sh
cd ../frontend
npm install
npm start
```

