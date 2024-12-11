# Autism Diagnosis REST API

A REST API that can be used to diagnose autism in adults. In this project, a decision tree algorithm is used to diagnose autism.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Flask

## Getting Started

### Installation

Here are the steps to run this project on your local computer.

1. Give a star to this repo.
2. Clone this repo.
   ```sh
   git clone https://github.com/zulfikarpinem/autism_diagnosis_api.git
   ```
3. Change current working dir to `/autism_diagnosis_api`.
4. Get all requirements.
   ```sh
   pip install -r requirements.txt
   ```
5. Run the server.
   ```sh
   python3 app.py
   ```

### Usage

#### Questions

- **Endpoint**
  ```http
  GET /questions
  ```
- **Response**
  ```json
  [
      {
          "id": "1",
          "question": "Saya sering mendengar suara-suara kecil ketika orang lain tidak mendengarnya"
      },
      ...
      {
          "id": "10",
          "question": "Saya merasa sulit untuk mengetahui niat orang lain"
      }
  ]
  ```

#### Diagnosis

- **Endpoint**
  ```http
  POST /diagnosis
  ```
- **Request** (Example)

  ```json
  {
    "A1": 1,
    "A2": 1,
    "A3": 0,
    "A4": 1,
    "A5": 1,
    "A6": 1,
    "A7": 0,
    "A8": 0,
    "A9": 1,
    "A10": 1
  }
  ```

- **Response**
  ```json
  {
    "message": "Anda kemungkinan mengidap autisme.",
    "result": "Autisme"
  }
  ```

---

## Author

- [Mhd Zulfikar Pinem](https://github.com/zeddlabs)

## Contact

- Email : zulfikarm022@gmail.com
