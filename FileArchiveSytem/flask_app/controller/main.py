from flask import render_template, request, redirect, session, Flask 
from flask_app import app
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os
from googleapiclient.http import MediaFileUpload
from flask import flash


@app.route('/')
def main():


    return render_template('main.html')


# @app.route('/createSharedDrive',methods=["POST"])
# def createSharedDrive():

#     scope = 'https://www.googleapis.com/auth/drive.file'

#     credentials = ServiceAccountCredentials.from_json_keyfile_name('skey.json', scope)
#     http = httplib2.Http()

#     drive_service = build('drive', 'v3', http=credentials.authorize(http))
#     name = request.form['name']
#     folderID = request.form['folderID']

#     file_metadata = {
#         'parents' : [folderID],
#         'name': name,
#         'mimeType': 'application/vnd.google-apps.folder',
#     }
#     file = drive_service.files().create(body=file_metadata,supportsAllDrives=True,
#                                         fields='id').execute()
#     print('Folder ID: %s' % file.get('id'))
#     session['newFolderID'] = file.get('id')
#     flash ("Congratulations you have succesfully created a new Shared Drive Folder", "newShared")

#     return redirect('/', )

# @app.route('/createSharedDrive',methods=["POST"])
# def createSharedDrive():

#     scope = 'https://www.googleapis.com/auth/drive.file'

#     credentials = ServiceAccountCredentials.from_json_keyfile_name('skey.json', scope)
#     http = httplib2.Http()

#     drive_service = build('drive', 'v3', http=credentials.authorize(http))
#     name = request.form['name']
#     # folderID = request.form['folderID']

#     file_metadata = {
#         'parents' : ['Insert the location of where the files will be uploaded too'],
#         'name': name,
#         'mimeType': 'application/vnd.google-apps.folder',
#     }
#     file = drive_service.files().create(body=file_metadata,supportsAllDrives=True,
#                                         fields='id').execute()
#     print('Folder ID: %s' % file.get('id'))
#     session['newFolderID'] = file.get('id')
#     flash ("Congratulations you have succesfully created a new Shared Drive Folder", "newShared")

#     return redirect('/', )

# @app.route('/uploadFiles', methods=['POST'])
# def uploadFiles():
#     scope = 'https://www.googleapis.com/auth/drive.file'

#     drive_service = build('drive', 'v3', credentials = ServiceAccountCredentials.from_json_keyfile_name('skey.json', scope))
    
#     location = request.form['location']
#     id = session['newFolderID']

#     path = location

#     # '/Users/Marvin Diaz/Desktop/RandomFIles/'

#     for x in os.listdir(path):
#         file_metadata = {
#             'name': x,
#             # 'mimeType': 'application/zip',
#             'parents': [id]}

#         ##########   EXAMPLE OF HOW WE WOULD SPECIFY THE MIMETYPE  #############
#         # media = MediaFileUpload(os.path.join(path,x), mimetype='application/zip')

#         media = MediaFileUpload(os.path.join(path,x))

#         f = drive_service.files().create(
#             body=file_metadata, media_body=media, supportsAllDrives=True).execute()

#         print("Created file '%s' id '%s'." % (f.get('name'), f.get('id')))
#         flash (f"Congratulations you have succesfully uploaded: {x}", "newUpload")

#     return redirect('/')




@app.route('/createSharedDrive',methods=["POST"])
def createSharedDrive():

    scope = 'https://www.googleapis.com/auth/drive.file'

    credentials = ServiceAccountCredentials.from_json_keyfile_name('skey.json', scope)
    http = httplib2.Http()

    drive_service = build('drive', 'v3', http=credentials.authorize(http))
    name = request.form['name']
    # folderID = request.form['folderID']

    file_metadata = {
        'parents' : ['Insert the location of where the files will be uploaded too'],
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
    }
    file = drive_service.files().create(body=file_metadata,supportsAllDrives=True,
                                        fields='id').execute()
    print('Folder ID: %s' % file.get('id'))
    session['newFolderID'] = file.get('id')
    flash ("Congratulations you have succesfully created a new Shared Drive Folder", "newShared")

    scope = 'https://www.googleapis.com/auth/drive.file'

    drive_service = build('drive', 'v3', credentials = ServiceAccountCredentials.from_json_keyfile_name('skey.json', scope))
    
    location = request.form['location']
    id = session['newFolderID']

    path = location

    # '/Users/Marvin Diaz/Desktop/RandomFIles/'

    for x in os.listdir(path):
        file_metadata = {
            'name': x,
            # 'mimeType': 'application/zip',
            'parents': [id]}

        ##########   EXAMPLE OF HOW WE WOULD SPECIFY THE MIMETYPE  #############
        # media = MediaFileUpload(os.path.join(path,x), mimetype='application/zip')

        media = MediaFileUpload(os.path.join(path,x))

        f = drive_service.files().create(
            body=file_metadata, media_body=media, supportsAllDrives=True).execute()

        print("Created file '%s' id '%s'." % (f.get('name'), f.get('id')))
        flash (f"Congratulations you have succesfully uploaded: {x}", "newUpload")

    return redirect('/')


