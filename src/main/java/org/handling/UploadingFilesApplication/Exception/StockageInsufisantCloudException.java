package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class StockageInsufisantCloudException extends CustomException{
  public StockageInsufisantCloudException(String message) {
    super(message, HttpStatus.INSUFFICIENT_STORAGE);
  }
}
