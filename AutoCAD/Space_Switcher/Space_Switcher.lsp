(defun switch-space ()
  (if (= (getvar 'cvport) 1) ; Check if current space is paper space
      (command "_mspace") ; Switch to model space
      (command "_pspace") ; Switch to paper space
  )
)

(defun C:SWITCHSPACE ()
  (command "_.undo" "_be") ; Begin undo group
  (switch-space)
  (command "_.undo" "_end") ; End undo group
  (princ)
)
