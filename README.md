# Church Financial Management System

## Overview
The **Church Financial Management System** is a web-based application designed to help churches efficiently track and manage their financial transactions, including tithes, offerings, expenses, and budgets. The system ensures transparency and accountability in financial management by providing real-time insights into the church's financial status.

## Features
### **1. User Management**
- Admin authentication and role-based access control
- Secure login and logout functionality
- Role-based permissions (Admin, Treasurer, Member, Auditor)

### **2. Income Management**
- Record and categorize tithes and offerings
- Track donations from members and external sources
- Generate financial reports on income sources

### **3. Expense Management**
- Log church expenses such as utilities, salaries, maintenance, and outreach programs
- Categorize expenses for better tracking
- Approve or reject expenses based on predefined policies

### **4. Budgeting and Financial Planning**
- Set yearly and monthly budgets
- Track actual expenses against the budget
- Generate variance analysis reports

### **5. Reports & Analytics**
- Income vs Expense reports
- Custom financial reports (e.g., by category, member, or period)
- Graphical dashboard for real-time insights

### **6. Member Contributions**
- Maintain individual member contributions
- Generate giving statements for members
- Track pledges and commitments

### **7. Payment & Bank Integration**
- Record bank deposits and withdrawals
- Integration with mobile money and online payment gateways
- Reconciliation of transactions

### **8. Audit & Compliance**
- Maintain a transaction log for accountability
- Export financial reports for audits
- Enforce financial policies and approval workflows

## Technology Stack
### **Backend**
- **Django (Python)** – Backend framework for handling business logic
- **Django REST Framework** – API development for frontend integration
- **PostgreSQL/MySQL** – Database for storing financial data

### **Frontend**
- **HTML, CSS, JavaScript (Bootstrap)** – User Interface
- **Vue.js or React.js** (optional) – For interactive UI components

### **Other Tools & Integrations**
- **Celery & Redis** – Background task processing (e.g., scheduled reports)
- **Docker** – Containerization for easy deployment
- **Nginx & Gunicorn** – Server deployment

## Installation Guide
### **1. Prerequisites**
Ensure you have the following installed on your system:
- Python 3.x
- PostgreSQL/MySQL
- Node.js & npm (for frontend development)
- Redis (for background tasks)

### **2. Clone the Repository**
```bash
git clone https://github.com/dihfahsih1/church-financial-management.git
cd church-financial-management
```

### **3. Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file and add the following:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/church_finance
ALLOWED_HOSTS=127.0.0.1,localhost
```

### **5. Run Database Migrations**
```bash
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### **6. Run the Development Server**
```bash
python manage.py runserver
```

### **7. Run Frontend (If Using Vue.js or React)**
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/login/` | POST | User login |
| `/api/auth/register/` | POST | User registration |
| `/api/incomes/` | GET | List all incomes |
| `/api/incomes/create/` | POST | Create a new income entry |
| `/api/expenses/` | GET | List all expenses |
| `/api/expenses/create/` | POST | Add a new expense |
| `/api/reports/` | GET | Generate financial reports |

## Deployment
### **Using Docker**
```bash
docker-compose up --build -d
```

### **Using Gunicorn & Nginx**
```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 church_finance.wsgi:application
```

## Security Considerations
- Use **HTTPS** in production (configure Nginx with SSL)
- Enable **Two-Factor Authentication (2FA)** for admin users
- Implement **Role-Based Access Control (RBAC)**
- Regularly update dependencies to fix vulnerabilities

## Contributing
We welcome contributions! Follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your fork (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License.

## Contact & Support
- **Email**: support@churchfinance.com
- **Website**: [churchfinance.com](http://churchfinance.com)
- **GitHub Issues**: Open an issue for bug reports and feature requests
