
import streamlit as st
import time

st.title("To jest strona Iwony Milewskiej")
col1, col2 = st.columns([1, 1])

uploades_photo = col2.file_uploader("Upload a photo")
col1.image("Iwonka_plaza_siedzaca_Emilia.jpg")

with st.expander("Code (expander)"):
    st.code('''
    @app.route('/process', methods=['POST'])
    def process_data():
        content = request.json
        if content and 'value' in content:
            processed_data = {'result': content['value'] * 2}
            return jsonify(processed_data)  # Upewnij się, że zwracasz JSON
        else:
            return jsonify({'error': 'Invalid input'}), 400  # Obsłuż błędne dane wejściowe''', language='python')
