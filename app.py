import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from utils.pdf_reader import extract_text_from_pdf
from utils.vector_store import create_vectorstore
from utils.rag_chain import build_qa_chain

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
OPENAI_API_KEY="put your key"
# Replace with your actual API key

vectorstore = None
qa_chain = None

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    global vectorstore, qa_chain
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file part", 400
        file = request.files['resume']
        if file.filename == '':
            return "No selected file", 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text from PDF
        text = extract_text_from_pdf(file_path)

        # Create vectorstore and QA chain
        vectorstore = create_vectorstore(text, OPENAI_API_KEY)
        qa_chain = build_qa_chain(vectorstore, OPENAI_API_KEY)

        return render_template('chat.html')

    return render_template('upload.html')


@app.route('/ask', methods=['POST'])
def ask():
    global qa_chain
    if not qa_chain:
        return jsonify({'error': 'No resume uploaded yet.'}), 400

    data = request.get_json()
    question = data.get('question', '').strip()

    if not question:
        return jsonify({'error': 'Please provide a question.'}), 400

    answer = qa_chain.run(question)
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)
