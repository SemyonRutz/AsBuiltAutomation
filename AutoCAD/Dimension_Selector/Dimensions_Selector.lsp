(defun c:SELDIMS ()
  (setq searchString (getstring "\nEnter the word to search for: "))
  (if (not (equal searchString ""))
    (progn
      (setq rows '())
      (setq dimEnts (ssget "_X" '((0 . "DIMENSION"))))
      (if dimEnts
        (progn
          (setq totalDim (sslength dimEnts))
          (setq i 0)
          (while (< i totalDim)
            (setq ent (ssname dimEnts i))
            (setq dimText (cdr (assoc 1 (entget ent))))
            (if (vl-string-search searchString dimText)
              (setq rows (cons ent rows)))
            (setq i (1+ i))
          )
          (if rows
            (progn
              (setq rowsSS (ssadd))
              (foreach row rows
                (ssadd row rowsSS)
              )
              (command "_.select" rowsSS)
            )
            (prompt (strcat "\nNo dimensions containing '" searchString "' found."))
          )
        )
      )
    )
  )
  (princ)
)

(c:SelectDimensionsContainingWord) ; Call the function
