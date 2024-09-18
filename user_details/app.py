from datetime import datetime
import os
from flask import jsonify, request, render_template
from werkzeug.utils import secure_filename
from __init__ import app, db
from model import User,Technical,Modules,Manuals,Machine_form,Layers,Cards,Machine,Iodata

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

        return jsonify({ "message": "technical_details added successfully",}),200

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

        return jsonify({ "message": "modules details added successfully",}),200

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

        return jsonify({"message": "manuals details added successfully", }), 200

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


@app.route("/layers",methods = ['GET','POST'])
def layers():
    if request.method == 'POST':
        layer_type = request.form.get('layer_type')
        layer_name = request.form.get('layer_name')
        company_logo = request.form.get('company_logo')
        location = request.form.get('location')

        if not layer_type or not layer_name or not company_logo or not location:
            return jsonify({"error": "Missing required fields"}), 400

        print(f"layer_type: {layer_type},layer_name: {layer_name},company_logo: {company_logo},location: {location}")

        try:
            layers_data = Layers(layer_type=layer_type,layer_name=layer_name,company_logo=company_logo,location=location)
            layers_data.save()
        except Exception as e:
            print(f"Error saving machine details: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message": "layers details added successfully"}), 200

    return render_template("layers.html")

@app.route("/cards",methods = ['GET','POST'])
def cards_inventory():
    if request.method == 'POST':
        card_type = request.form.get('card_type')

        if not card_type:
            return jsonify({"error": "Missing required fields"}), 400

        print(f"cards_type: {card_type}")

        try:
            cards_data = Cards(card_type=card_type)
            cards_data.save()

        except Exception as e:
            print(f"Error saving machine details: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message": "cards details added successfully"}), 200

    return render_template("cards.html")


@app.route("/machine_list",methods = ['GET','POSt'])
def machine_card_list():
    if request.method == 'POST':
        machine_id = request.form.get('machine_id')
        kpi_name = request.form.get('kpi_name')
        datapoints = request.form.get('datapoints')
        mode = request.form.get('mode')
        conversion = request.form.get('conversion')
        x_label = request.form.get('x_label')
        y_label = request.form.get('y_label')
        ledger = request.form.get('ledger')
        title = request.form.get('title')
        card_type = request.form.get('card_type')
        unit = request.form.get('unit')

        if not machine_id or not kpi_name or not datapoints or not mode or not conversion or not x_label or not y_label or not ledger or not title or not card_type or not unit:
            return jsonify({"error": "Missing required fields"}), 400

        try:
            machine_data = Machine(machine_id=machine_id,kpi_name=kpi_name,datapoints=datapoints,mode=mode,conversion=conversion,x_label=x_label,y_label=y_label,ledger=ledger,title=title,card_type=card_type,unit=unit)
            machine_data.save()


        except Exception as e:
            print(f"Error saving machine details: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message": "machine details added successfully"}), 200

    return render_template("machine_list.html")



@app.route("/io_list",methods = ['GET','POST'])
def io_list():
    if request.method == 'POST':
        io_group = request.form.get('io_group')
        io_type = request.form.get('io_type')
        io_name = request.form.get('io_name')
        io_value = request.form.get('io_value')
        io_color = request.form.get('io_color')
        io_range = request.form.get('io_range')
        io_unit = request.form.get('io_unit')
        control = request.form.get('control') == 'true'
        alarm = request.form.get('alarm') == 'true'

        if not io_group or not io_type or not io_name or not io_value or not io_color or not io_range or not io_unit:
            return jsonify({"error": "Missing required fields"}), 400

        try:
            data_io = Iodata(io_group=io_group,io_type=io_type,io_name=io_name,io_value=io_value,io_color=io_color,io_range=io_range,io_unit=io_unit,control=control,alarm=alarm)
            data_io.save()
        except Exception as e:
            print(f"Error saving machine details: {e}")
            return jsonify({"error": "An error occurred while saving to the database"}), 500

        return jsonify({"message":"Io_data  added successfully"}), 200

    return render_template("io_list.html")





if __name__ == '__main__':
    app.run(debug=True)
