package org.handling.UploadingFilesApplication.Exception;

public class FileTooLargeException extends RuntimeException{
  public FileTooLargeException(String message) {
    super(message);
  }
}
