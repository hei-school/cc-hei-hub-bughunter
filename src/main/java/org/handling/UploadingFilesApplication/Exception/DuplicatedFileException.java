package org.handling.UploadingFilesApplication.Exception;

import org.springframework.http.HttpStatus;

public class DuplicatedFileException extends CustomException {
  public DuplicatedFileException(String message) {
    super(message, HttpStatus.CONFLICT);
  }
}

