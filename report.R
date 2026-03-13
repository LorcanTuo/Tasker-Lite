# IT Tasker - R Report Generator
# Args: walkin.csv  escalated.csv  out_dir  start_date  end_date

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 5) stop("Usage: Rscript report.R <walkin.csv> <escalated.csv> <out_dir> <start> <end>")

walkin_csv   <- args[1]
escalated_csv <- args[2]
out_dir      <- args[3]
start_dt     <- args[4]
end_dt       <- args[5]

# ── Install missing packages silently ────────────────────────────────────────
required <- c("ggplot2", "scales")
for (pkg in required) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org", quiet = TRUE)
  }
  suppressPackageStartupMessages(library(pkg, character.only = TRUE))
}

# ── Helper: save a ggplot to <out_dir>/<filename>.png ────────────────────────
save_chart <- function(p, filename, width = 8, height = 5) {
  ggsave(
    filename = file.path(out_dir, filename),
    plot     = p,
    width    = width,
    height   = height,
    dpi      = 150,
    bg       = "white"
  )
}

# ── Theme ─────────────────────────────────────────────────────────────────────
gc_theme <- theme_minimal(base_size = 13) +
  theme(
    plot.title       = element_text(face = "bold", size = 14, margin = margin(b = 8)),
    plot.subtitle    = element_text(colour = "#555555", size = 11),
    axis.title       = element_text(size = 11),
    panel.grid.minor = element_blank(),
    plot.background  = element_rect(fill = "white", colour = NA)
  )
theme_set(gc_theme)

gc_blue  <- "#1a3a5c"
gc_blue2 <- "#4a90d9"
gc_red   <- "#c0392b"
col_prog <- "#f0a500"
col_done <- "#27ae60"

# ── Read CSVs (allow empty files) ────────────────────────────────────────────
safe_read <- function(path, ...) {
  if (!file.exists(path) || file.info(path)$size == 0) return(data.frame())
  read.csv(path, stringsAsFactors = FALSE, ...)
}

walkin    <- safe_read(walkin_csv)
escalated <- safe_read(escalated_csv)

# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 – Walk-in Tickets by Category
# ══════════════════════════════════════════════════════════════════════════════
if (nrow(walkin) > 0 && "category" %in% names(walkin)) {
  td <- as.data.frame(table(category = walkin$category), stringsAsFactors = FALSE)
  td <- td[td$category != "" & !is.na(td$category), ]
  td <- td[order(td$Freq), ]
  td$category <- factor(td$category, levels = td$category)

  p1 <- ggplot(td, aes(x = category, y = Freq, fill = Freq)) +
    geom_col(show.legend = FALSE) +
    geom_text(aes(label = Freq), hjust = -0.2, size = 3.5) +
    coord_flip() +
    scale_fill_gradient(low = gc_blue2, high = gc_blue) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.15))) +
    labs(
      title    = "Walk-in Tickets by Category",
      subtitle = paste("Period:", start_dt, "to", end_dt),
      x        = NULL, y = "Count"
    )
  save_chart(p1, "chart_categories.png", width = 8, height = max(4, nrow(td) * 0.5 + 2))
}

# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 – Walk-in Tickets Over Time
# ══════════════════════════════════════════════════════════════════════════════
if (nrow(walkin) > 0 && "date" %in% names(walkin)) {
  walkin$date_parsed <- suppressWarnings(as.Date(walkin$date))
  walkin_dates <- walkin[!is.na(walkin$date_parsed), ]

  if (nrow(walkin_dates) > 0) {
    td2 <- as.data.frame(table(date = walkin_dates$date_parsed))
    td2$date <- as.Date(td2$date)

    p2 <- ggplot(td2, aes(x = date, y = Freq)) +
      geom_line(colour = gc_blue, linewidth = 1) +
      geom_point(colour = gc_blue, size = 2.5, fill = "white", shape = 21, stroke = 1.5) +
      scale_x_date(date_labels = "%d %b", date_breaks = "1 week") +
      scale_y_continuous(breaks = scales::breaks_pretty()) +
      labs(
        title    = "Walk-in Tickets Over Time",
        subtitle = paste("Period:", start_dt, "to", end_dt),
        x        = NULL, y = "Tickets per Day"
      ) +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    save_chart(p2, "chart_timeline.png")
  }
}

# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 – Status Breakdown by Type
# ══════════════════════════════════════════════════════════════════════════════
build_status <- function(df, label) {
  if (nrow(df) == 0 || !"status" %in% names(df)) return(data.frame())
  data.frame(category = label, status = df$status, stringsAsFactors = FALSE)
}

status_all <- rbind(
  build_status(walkin,    "Walk-in Tickets"),
  build_status(escalated, "Escalated Tickets")
)

if (nrow(status_all) > 0) {
  td3 <- as.data.frame(table(category = status_all$category, status = status_all$status))
  td3$status <- factor(td3$status, levels = c("IN PROGRESS", "RESOLVED"))

  p3 <- ggplot(td3, aes(x = category, y = Freq, fill = status)) +
    geom_col(position = "dodge", width = 0.6) +
    geom_text(aes(label = ifelse(Freq > 0, Freq, "")),
              position = position_dodge(width = 0.6), vjust = -0.4, size = 3.5) +
    scale_fill_manual(
      values = c("IN PROGRESS" = col_prog, "RESOLVED" = col_done),
      labels = c("In Progress", "Resolved")
    ) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.15))) +
    labs(
      title    = "Status Breakdown by Type",
      subtitle = paste("Period:", start_dt, "to", end_dt),
      x        = NULL, y = "Count", fill = NULL
    ) +
    theme(legend.position = "top")
  save_chart(p3, "chart_status.png")
}

# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 – Escalated Tickets by Area
# ══════════════════════════════════════════════════════════════════════════════
if (nrow(escalated) > 0 && "area" %in% names(escalated)) {
  td4 <- as.data.frame(table(area = escalated$area), stringsAsFactors = FALSE)
  td4 <- td4[td4$area != "" & !is.na(td4$area), ]

  if (nrow(td4) > 0) {
    td4 <- td4[order(td4$Freq), ]
    td4$area <- factor(td4$area, levels = td4$area)

    p4 <- ggplot(td4, aes(x = area, y = Freq, fill = Freq)) +
      geom_col(show.legend = FALSE) +
      geom_text(aes(label = Freq), hjust = -0.2, size = 3.5) +
      coord_flip() +
      scale_fill_gradient(low = "#e07b6e", high = gc_red) +
      scale_y_continuous(expand = expansion(mult = c(0, 0.15))) +
      labs(
        title    = "Escalated Tickets by Area",
        subtitle = paste("Period:", start_dt, "to", end_dt),
        x        = NULL, y = "Count"
      )
    save_chart(p4, "chart_escalated_area.png", width = 8, height = max(4, nrow(td4) * 0.5 + 2))
  }
}

cat("OK\n")
