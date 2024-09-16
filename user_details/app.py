import os
from flask import jsonify, request, render_template
from werkzeug.utils import secure_filename
from __init__ import app, db
from model import User

# Define upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the uploaded file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle form submission and file upload
@app.route("/user_details", methods=['GET', 'POST'])
def user_details():
    if request.method == 'POST':
        # Check if the photo is uploaded
        if 'photo' not in request.files:
            return jsonify({"error": "No photo uploaded"}), 400

        photo = request.files['photo']
        if photo.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Validate the file type
        if not allowed_file(photo.filename):
            return jsonify({"error": "Invalid file type"}), 400

        # Save the uploaded file securely
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)

        # Get the relative path to store in the database
        relative_photo_path = os.path.join(UPLOAD_FOLDER, filename)

        # Retrieve form data
        user_id = request.form.get('user_id')
        mobile_no = request.form.get('mobile_no')
        company_id = request.form.get('company_id')

        if not user_id or not mobile_no or not company_id:
            return jsonify({"error": "Missing required fields"}), 400

        # Debugging: Print the values being saved
        print(f"user_id: {user_id}, photo: {relative_photo_path}, mobile_no: {mobile_no}, company_id: {company_id}")

        # Save data to the database
        try:
            record = User(user_id=user_id, photo=relative_photo_path, mobile_no=mobile_no, company_id=company_id)
            record.save()
        except Exception as e:
            # Log and return the error if something goes wrong
            print(f"Error saving user: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({
            "message": "User details added successfully",
            "user_id": user_id,
            "photo": relative_photo_path,
            "mobile_no": mobile_no,
            "company_id": company_id
        }), 200

    # Render the form for a GET request
    return render_template("us.html")

if __name__ == '__main__':
    app.run(debug=True)
