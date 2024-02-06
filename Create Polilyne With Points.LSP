(defun c:CPFB ()
 (setq block-points '())

 (prompt "\nSelect Block Reference Points:")
 (setq ss (ssget "_:L" '((0 . "INSERT"))))

 (if ss
     (progn
       (setq i 0)
       (repeat (sslength ss)
         (setq ent (ssname ss i))
         (setq i (1+ i))
         (setq pt (cdr (assoc 10 (entget ent))))
         (setq block-points (cons pt block-points))
       )

       (command "PLINE")
       (foreach point block-points
         (command point)
       )

       (command "")
     )
     (prompt "\nNo Block Reference points found.")
   )
)