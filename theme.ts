import { darken, desaturate, lighten, readableColor, transparentize } from 'polished';

export const theme: ThemeInterface = {
  spacing: {
    unit: 5,
    sectionHorizontal: ({ spacing }) => spacing.unit * 8,
    sectionVertical: ({ spacing }) => spacing.unit * 8,
  },
  breakpoints: {
    small: '50rem',
    medium: '75rem',
    large: '105rem',
  },
  colors: {
    tonalOffset: 0.2,
    primary: {
      main: '#32329f',
      light: ({ colors }) => lighten(colors.tonalOffset, colors.primary.main),
      dark: ({ colors }) => darken(colors.tonalOffset, colors.primary.main),
      contrastText: ({ colors }) => readableColor(colors.primary.main),
    },
    success: {
      main: '#1d8127',
      light: ({ colors }) => lighten(colors.tonalOffset * 2, colors.success.main),
      dark: ({ colors }) => darken(colors.tonalOffset, colors.success.main),
      contrastText: ({ colors }) => readableColor(colors.success.main),
    },
    warning: {
      main: '#ffa500',
      light: ({ colors }) => lighten(colors.tonalOffset, colors.warning.main),
      dark: ({ colors }) => darken(colors.tonalOffset, colors.warning.main),
      contrastText: '#ffffff',
    },
    error: {
      main: '#d41f1c',
      light: ({ colors }) => lighten(colors.tonalOffset, colors.error.main),
      dark: ({ colors }) => darken(colors.tonalOffset, colors.error.main),
      contrastText: ({ colors }) => readableColor(colors.error.main),
    },
    gray: {
      50: '#FAFAFA',
      100: '#F5F5F5',
    },
    text: {
      primary: '#333333',
      secondary: ({ colors }) => lighten(colors.tonalOffset, colors.text.primary),
    },
    border: {
      dark: 'rgba(0,0,0, 0.1)',
      light: '#ffffff',
    },
    responses: {
      success: {
        color: ({ colors }) => colors.success.main,
        backgroundColor: ({ colors }) => transparentize(0.93, colors.success.main),
        tabTextColor: ({ colors }) => colors.responses.success.color,
      },
      error: {
        color: ({ colors }) => colors.error.main,
        backgroundColor: ({ colors }) => transparentize(0.93, colors.error.main),
        tabTextColor: ({ colors }) => colors.responses.error.color,
      },
      redirect: {
        color: ({ colors }) => colors.warning.main,
        backgroundColor: ({ colors }) => transparentize(0.9, colors.responses.redirect.color),
        tabTextColor: ({ colors }) => colors.responses.redirect.color,
      },
      info: {
        color: '#87ceeb',
        backgroundColor: ({ colors }) => transparentize(0.9, colors.responses.info.color),
        tabTextColor: ({ colors }) => colors.responses.info.color,
      },
    },
    http: {
      get: '#2F8132',
      post: '#186FAF',
      put: '#95507c',
      options: '#947014',
      patch: '#bf581d',
      delete: '#cc3333',
      basic: '#707070',
      link: '#07818F',
      head: '#A23DAD',
    },
  },
  schema: {
    linesColor: theme =>
      lighten(
        theme.colors.tonalOffset,
        desaturate(theme.colors.tonalOffset, theme.colors.primary.main),
      ),
    defaultDetailsWidth: '75%',
    typeNameColor: theme => theme.colors.text.secondary,
    typeTitleColor: theme => theme.schema.typeNameColor,
    requireLabelColor: theme => theme.colors.error.main,
    labelsTextSize: '0.9em',
    nestingSpacing: '1em',
    nestedBackground: '#fafafa',
    arrow: {
      size: '1.1em',
      color: theme => theme.colors.text.secondary,
    },
  },
  typography: {
    fontSize: '14px',
    lineHeight: '1.5em',
    fontWeightRegular: '400',
    fontWeightBold: '600',
    fontWeightLight: '300',
    fontFamily: 'Roboto, sans-serif',
    smoothing: 'antialiased',
    optimizeSpeed: true,
    headings: {
      fontFamily: 'Montserrat, sans-serif',
      fontWeight: '400',
      lineHeight: '1.6em',
    },
    code: {
      fontSize: '13px',
      fontFamily: 'Courier, monospace',
      lineHeight: ({ typography }) => typography.lineHeight,
      fontWeight: ({ typography }) => typography.fontWeightRegular,
      color: '#e53935',
      backgroundColor: 'rgba(38, 50, 56, 0.05)',
      wrap: false,
    },
    links: {
      color: ({ colors }) => colors.primary.main,
      visited: ({ typography }) => typography.links.color,
      hover: ({ typography }) => lighten(0.2, typography.links.color),
      textDecoration: 'auto',
      hoverTextDecoration: 'auto',
    },
  },
  sidebar: {
    width: '260px',
    backgroundColor: '#fafafa',
    textColor: '#333333',
    activeTextColor: theme =>
      theme.sidebar.textColor !== theme.sidebar!.textColor
        ? theme.sidebar.textColor
        : theme.colors.primary.main,
    groupItems: {
      activeBackgroundColor: theme => darken(0.1, theme.sidebar.backgroundColor),
      activeTextColor: theme => theme.sidebar.activeTextColor,
      textTransform: 'uppercase',
    },
    level1Items: {
      activeBackgroundColor: theme => darken(0.05, theme.sidebar.backgroundColor),
      activeTextColor: theme => theme.sidebar.activeTextColor,
      textTransform: 'none',
    },
    arrow: {
      size: '1.5em',
      color: theme => theme.sidebar.textColor,
    },
  },
  logo: {
    maxHeight: ({ sidebar }) => sidebar.width,
    maxWidth: ({ sidebar }) => sidebar.width,
    gutter: '2px',
  },
  rightPanel: {
    backgroundColor: '#263238',
    width: '40%',
    textColor: '#ffffff',
    servers: {
      overlay: {
        backgroundColor: '#fafafa',
        textColor: '#263238',
      },
      url: {
        backgroundColor: '#fff',
      },
    },
  },
  codeBlock: {
    backgroundColor: ({ rightPanel }) => darken(0.1, rightPanel.backgroundColor),
  },
  fab: {
    backgroundColor: '#f2f2f2',
    color: '#0065FB',
  },
};
