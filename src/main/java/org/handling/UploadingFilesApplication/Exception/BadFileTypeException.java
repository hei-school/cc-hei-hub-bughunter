package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class BadFileTypeException extends CustomException {
  public BadFileTypeException(String message) {
    super(message, HttpStatus.BAD_REQUEST);
  }
}
