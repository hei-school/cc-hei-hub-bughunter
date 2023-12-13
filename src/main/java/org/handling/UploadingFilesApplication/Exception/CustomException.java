package org.handling.UploadingFilesApplication.Exception;

import lombok.Getter;
import org.springframework.http.HttpStatus;

@Getter
public class CustomException extends RuntimeException {

  private final HttpStatus code;

  public CustomException(String message, HttpStatus code){
    super(message);
    this.code = code;
  }
}