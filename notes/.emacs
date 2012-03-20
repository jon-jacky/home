;;; For showing simple text "slides" in a text file with +-- separators

(defun slide ()
  "Advance to next slide"
  (interactive)
  (search-forward "+-") ; start-of-slide marker
  (recenter 0))         ; move point to top of window

(defun bslide ()
  "Return to previous slide"
  (interactive)
  (search-backward "+-") ; start-of-slide marker
  (recenter 0))         ; move point to top of window

(global-set-key [f5] 'bslide) ; "backm, previous slide" key to the left
(global-set-key [f6] 'slide)  ; "forward, next slide" key to the right

;;; For switching between several windows using arrow keys,
;;; more convient than C-x o when there are more than two windows

;;; This does not work in Mac emacs, apparently because it runs in terminal
;;; (when (fboundp 'windmove-default-keybindings)
;;;      (windmove-default-keybindings))

;;; This does work on Mac, reported to work in terminal other OS: emacs -nw 
(global-set-key (kbd "C-c <left>")  'windmove-left)
(global-set-key (kbd "C-c <right>") 'windmove-right)
(global-set-key (kbd "C-c <up>")    'windmove-up)
(global-set-key (kbd "C-c <down>")  'windmove-down)
