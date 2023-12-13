package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class FileTooLargeException extends CustomException{
  public FileTooLargeException(String message) {
    super(message, HttpStatus.PAYLOAD_TOO_LARGE);
  }
}
