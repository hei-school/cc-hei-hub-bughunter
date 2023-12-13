package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class StorageInsufisantException extends CustomException{
  public StorageInsufisantException(String message) {
    super(message, HttpStatus.INSUFFICIENT_STORAGE);
  }
}
