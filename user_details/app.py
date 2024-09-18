from datetime import datetime
import os
from flask import jsonify, request, render_template
from werkzeug.utils import secure_filename
from __init__ import app, db
from model import User,Technical,Modules,Manuals,Machine_form

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


@app.route("/add_technical", methods=['GET', 'POST'])
def technical_details():
    if request.method == 'POST':

        item_name = request.form.get('item_name')
        manufacture_name = request.form.get('manufacture_name')
        manufacture_model_no = request.form.get('manufacture_model_no')
        expiry_date = request.form.get('expiry_date')

        # Debugging: Print the values being saved
        print(f"item_name: {item_name}, manufacture_name: {manufacture_name}, manufacture_model_no: {manufacture_model_no},expiry_date: {expiry_date}")

        # Save data to the database
        try:
            technical_data = Technical(item_name=item_name, manufacture_name=manufacture_name, manufacture_model_no=manufacture_model_no, expiry_date=expiry_date)
            technical_data.save()
        except Exception as e:
            # Log and return the error if something goes wrong
            print(f"Error saving user: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({ "message": "User details added successfully",}),200

    return render_template("tech.html")


@app.route("/modules", methods = ['GET','POST'])
def modules():
    if request.method == 'POST':

        module_name = request.form.get('module_name')
        icons = request.form.get('icons')
        type = request.form.get('type')


        if not module_name or not icons or not type:
            return jsonify({"error": "Missing required fields"}), 400

        print(f"module_name: {module_name},icons: {icons},type: {type}")


        try:
            module_data = Modules(module_name=module_name, icons=icons, type=type)
            module_data.save()
        except Exception as e:
            # Log and return the error if something goes wrong
            print(f"Error saving user: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({ "message": "User details added successfully",}),200

    return render_template("module.html")


@app.route("/manuals", methods = ['GET','POST'])
def manuals():
    if request.method == 'POST':
        filename = request.form.get('filename')
        fileurl = request.form.get('fileurl')

        if not filename or not fileurl :
            return jsonify({"error": "Missing required fields"}), 400

        print(f"filename: {filename},fileurl: {fileurl}")

        try:
            manuals_data = Manuals(filename=filename, fileurl=fileurl)
            manuals_data.save()
        except Exception as e:
            # Log and return the error if something goes wrong
            print(f"Error saving user: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message": "User details added successfully", }), 200

    return render_template("manuals.html")

@app.route("/machine_details",methods = ['GET','POST'])
def machine_details():
    if request.method == 'POST':
        machine_id = request.form.get('machine_id')
        machine_name = request.form.get('machine_name')
        model_no = request.form.get('model_no')
        gateway_id = request.form.get('gateway_id')
        manual = request.form.get('manual')
        technical_table = request.form.get('technical_table')
        io_group_id = request.form.get('io_group_id')

        if not machine_id or not machine_name or not model_no or not gateway_id or not manual or not technical_table or not io_group_id:
            return jsonify({"error": "Missing required fields"}), 400

        print(
            f"machine_id: {machine_id}, machine_name: {machine_name}, model_no: {model_no}, gateway_id: {gateway_id}, manual: {manual}, technical_table: {technical_table}, io_group_id: {io_group_id}")

        try:
            machine_details_data = Machine_form(machine_id=machine_id, machine_name=machine_name,model_no=model_no, gateway_id=gateway_id, manual=manual,technical_table=technical_table, io_group_id=io_group_id)
            machine_details_data.save()
        except Exception as e:
            print(f"Error saving machine details: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message": "Machine details added successfully"}), 200

    return render_template("machine_details.html")


if __name__ == '__main__':
    app.run(debug=True)
