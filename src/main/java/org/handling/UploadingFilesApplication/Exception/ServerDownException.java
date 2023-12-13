package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class ServerDownException extends CustomException{
  public ServerDownException(String message) {
    super(message, HttpStatus.GATEWAY_TIMEOUT);
  }
}
