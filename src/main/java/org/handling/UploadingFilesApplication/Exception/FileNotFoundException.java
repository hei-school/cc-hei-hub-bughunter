package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class FileNotFoundException extends CustomException {

  public FileNotFoundException(String message) {
    super(message, HttpStatus.NOT_FOUND);
  }
}
