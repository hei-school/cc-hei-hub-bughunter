package org.handling.UploadingFilesApplication.controller;

import java.util.HashMap;
import java.util.Map;
import org.handling.UploadingFilesApplication.Exception.BadFileTypeException;
import org.handling.UploadingFilesApplication.Exception.CustomException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {
  @ExceptionHandler(value
      = CustomException.class)
  protected ResponseEntity<Object> handleConflict(CustomException exception) {
    Map<String, String> data = new HashMap<>();
    data.put("status", exception.getCode().toString());
    data.put("message", exception.getMessage());
    return new ResponseEntity<>(data,exception.getCode());
  }
}
