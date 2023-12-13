package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class NotImplementedException extends CustomException{
  public NotImplementedException(String message) {
    super(message, HttpStatus.NOT_IMPLEMENTED);
  }
}
